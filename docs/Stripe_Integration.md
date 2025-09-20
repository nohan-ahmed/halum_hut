# Stripe Integration Guide

## Setup

1. **Install Stripe SDK**:
   ```bash
   pip install stripe
   ```

2. **Configure Environment Variables**:
   ```env
   STRIPE_SECRET_KEY=sk_test_your_secret_key
   STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret
   ```

3. **Update Settings**:
   ```python
   import stripe
   stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
   ```

## Payment Flow

1. **Create Order**: POST `/orders/api/create-stripe-order/`
2. **Redirect to Checkout**: Use returned URL
3. **Webhook Confirmation**: Stripe calls `/orders/api/stripe-webhook/`
4. **Order Confirmed**: Payment and order status updated

## Webhook Configuration

Configure Stripe webhook endpoint:
- **URL**: `https://yourdomain.com/orders/api/stripe-webhook/`
- **Events**: `checkout.session.completed`

## Testing

Use Stripe test cards:
- Success: `4242424242424242`
- Decline: `4000000000000002`