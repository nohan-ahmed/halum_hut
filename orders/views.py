import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.throttling import UserRateThrottle, ScopedRateThrottle
from django.db import transaction
from django.utils import timezone

# Local Imports
from .models import Order, OrderItem, ShippingAddress, Payment
from .serializers import ShippingAddressSerializer, OrderSerializer
from cart.models import CartItem
from products.models import ProductVariant  # Handles product variants (e.g., size, color)
from core.paginations import StandardResultsSetPagination
from core.Permissions import IsOwner
from halum_hut.settings import STRIPE_API_KEY, STRIPE_WEBHOOK_SECRET

class ShippingAddressViewSet(ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = [IsOwner]
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['id', 'full_name', 'city', 'country']
    
    # Filters the queryset to include only shipping addresses for the current user.
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
    # Creates a shipping address for the current user.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# ------------------------------------------------------------------------------
# API endpoint to create an order using Cash On Delivery (COD) payment method.
# ------------------------------------------------------------------------------
# - Validates shipping address and cart items.
# - Creates an Order and associated OrderItems.
# - Updates product stock and creates a Payment record.
# - Clears the user's cart after order creation.
# - Returns order details on success.
# ------------------------------------------------------------------------------
# Future Considerations:
# - Add support for other payment methods.
# - Handle race conditions for stock updates (consider row-level locking).
# - Improve error handling for stock validation and payment creation.
# - Add notifications (email/SMS) after order creation.
# ------------------------------------------------------------------------------

class CreateOrderWithCOD(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'create_order'
    
    def post(self, request):
        user = request.user

        # Validate that a shipping address ID is provided in the request.
        shipping_data_id = request.data.get('shipping_address')
        if not shipping_data_id:
            return Response({"error": "Shipping address is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve the shipping address for the user.
        try:
            shipping_address = ShippingAddress.objects.get(user=user, id=shipping_data_id)
        except ShippingAddress.DoesNotExist:
            return Response({"error": "Shipping address does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch all cart items for the user.
        cart_items = CartItem.objects.filter(cart__user=user)
        if not cart_items.exists():
            return Response({"error": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)

        # Use a database transaction to ensure atomicity of order creation.
        with transaction.atomic():
            # Create the order with initial total_price=0 (will be updated below).
            order = Order.objects.create(
                user=user,
                shipping_address=shipping_address,
                total_price=0,  # Will be calculated after adding items.
                status='confirmed',  # COD orders are confirmed immediately.
            )

            total = 0  # Track total order price.

            # Iterate through cart items to create OrderItems and update stock.
            for item in cart_items:
                product_variant = item.variant

                # Check if enough stock is available for the requested quantity.
                if product_variant.stock < item.quantity:
                    # NOTE: Consider handling this error more gracefully in future.
                    return Response({"error": f"Not enough stock for product_variant: {product_variant.product.name}"}, status=status.HTTP_400_BAD_REQUEST)

                # Calculate item price and subtotal.
                price = product_variant.price  # Use current price as snapshot.
                subtotal = price * item.quantity

                # Create an OrderItem for each cart item.
                OrderItem.objects.create(
                    order=order,
                    product_variant=product_variant,
                    quantity=item.quantity,
                    price=price,
                    subtotal=subtotal
                )

                # Deduct purchased quantity from product stock.
                product_variant.stock -= item.quantity
                product_variant.save()

                total += subtotal  # Add to order total.

            # Update order with the final total price.
            order.total_price = total
            order.save()

            # Create a Payment record for COD.
            Payment.objects.create(
                order=order,
                user=user,
                method='cod',
                status='initiated',
                paid_at=None,  # COD payments are not paid upfront.
            )

            # Clear the user's cart after successful order creation.
            cart_items.delete()

        # Return order details in the response.
        return Response({
            "order_id": order.id,
            "status": order.status,
            "payment_method": "cod"
        }, status=status.HTTP_201_CREATED)


# stripe


stripe.api_key = STRIPE_API_KEY

class CreateOrderWithStripe(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        shipping_address_id = request.data.get('shipping_address')
        if not shipping_address_id:
            return Response({"error": "Shipping address is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve the shipping address for the user.
        try:
            shipping_address = ShippingAddress.objects.get(id=shipping_address_id)
        except ShippingAddress.DoesNotExist:
            return Response({"error": "Shipping address does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Fetch all cart items for the user.
        cart_items = CartItem.objects.filter(cart__user=request.user)
        if not cart_items.exists():
            return Response({"error": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Use a database transaction to ensure atomicity of order creation.
        with transaction.atomic():
            # Create the order with initial total_price=0 (will be updated below).
            order = Order.objects.create(
                user=request.user,
                shipping_address=shipping_address,
                total_price=0,  # Will be calculated after adding items.
                status='pending',  # stripe orders are pending initially.
            )
            
            
            total = 0  # Track total order price.
            products_details = []
            # Iterate through cart items to create OrderItems and update stock.
            for item in cart_items:
                product_variant = item.variant
                
                # Check if enough stock is available for the requested quantity.
                if product_variant.stock < item.quantity:
                    # NOTE: Consider handling this error more gracefully in future.
                    return Response({"error": f"Not enough stock for product_variant: {product_variant.product.name}"}, status=status.HTTP_400_BAD_REQUEST)
                
                # Calculate item price and subtotal.
                price = product_variant.price  # Use current price as snapshot.
                subtotal = price * item.quantity
                
                # Create an OrderItem for each cart item.
                OrderItem.objects.create(
                    order=order,
                    product_variant=product_variant,
                    quantity=item.quantity,
                    price=price,
                    subtotal=subtotal
                )
                
                # Add product details to the products_details list.
                products_details.append({
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': f'{product_variant.product.name} - {product_variant.sku}',
                        },
                        'unit_amount': int(price*100),  # Amount (in cents)
                    },
                    'quantity': item.quantity,
                })
                
                # Deduct purchased quantity from product stock.
                product_variant.stock -= item.quantity
                product_variant.save()
                
                total += subtotal  # Add to order total.
            
            # Update order with the final total price.
            order.total_price = total
            order.save()
            
            # Create a Payment record for Stripe.
            Payment.objects.create(
                order=order,
                user=request.user,
                method='stripe',
                status='initiated',
                paid_at=None,  # Stripe payments are not paid upfront.
            )
            

        # create a stripe checkout session
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=products_details, 
                mode='payment',
                metadata={'order_id': order.id},
                success_url=f"http://127.0.0.1:5500//success?session_id={{CHECKOUT_SESSION_ID}}",
                cancel_url=f"http://127.0.0.1:5500/cancel",
            )
            # Return the session ID and the checkout URL to the client
            return Response({'id': checkout_session.id, 'url': checkout_session.url})
        except Exception as e:
            return Response({'error': str(e)}, status=400)




endpoint_secret = STRIPE_WEBHOOK_SECRET

@csrf_exempt
def stripe_webhook_view(request):
    print("----- Webhook received! -----")
    print(endpoint_secret)
    payload = request.body
    sig_header = request.headers.get('stripe-signature')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    # Handle checkout session completed
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        
        # Get order ID from metadata
        order_id = session.get('metadata', {}).get('order_id')
        payment_intent_id = session.get('payment_intent')
        
        if order_id and payment_intent_id:
            try:
                payment = Payment.objects.get(
                    order_id=order_id,
                    method='stripe',
                    status='initiated'
                )
                
                # Update payment status
                payment.status = 'success'
                payment.transaction_id = payment_intent_id
                payment.paid_at = timezone.now()
                payment.save()
                
                # Update order status
                payment.order.status = 'confirmed'
                payment.order.save()
                
            except Payment.DoesNotExist:
                pass
    
    return HttpResponse(status=200)


# ------------------------------------------------------------------------------
# API endpoint to list all orders for the authenticated user.
# ------------------------------------------------------------------------------
# - Uses pagination for large order lists.
# - Only returns orders belonging to the requesting user.
# ------------------------------------------------------------------------------
# Future Considerations:
# - Add filtering (by status, date, etc.).
# - Support admin views for all orders.
# ------------------------------------------------------------------------------

class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwner]
    pagination_class = StandardResultsSetPagination
    throttle_classes = [UserRateThrottle]
    
    def get_queryset(self):
        user = self.request.user
        # Only return orders for the current user.
        return Order.objects.filter(user=user)
    

# ------------------------------------------------------------------------------
# API endpoint to retrieve and update a specific order.
# ------------------------------------------------------------------------------
# - Only allows access to orders owned by the requesting user.
# - Supports partial updates (PATCH) and full updates (PUT).
# ------------------------------------------------------------------------------
# Future Considerations:
# - Restrict updates to certain fields (e.g., status, address).
# - Add admin permissions for managing all orders.
# ------------------------------------------------------------------------------

class OrderUpdateDetail(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwner]
    throttle_classes = [UserRateThrottle]