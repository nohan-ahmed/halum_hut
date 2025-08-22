from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import UserRateThrottle, ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Local imports
from core.Permissions import IsAdminOrReadOnly
from core.paginations import StandardResultsSetPagination
from products.permissions import IsSellerOrReadOnly, IsSellerOrReadOnlyForProductData, IsSellerOrReadOnlyForVariantAttributeValue
from products import serializers, models

# Create your views here.


class BrandAPIView(ModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = [IsAdminOrReadOnly]  # Add your permission classes here if needed
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter]
    search_fields = ['id', 'name', 'slug']  # Adjust the fields you want to search on
    

class CategoryAPIView(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAdminOrReadOnly]  # Add your permission classes here if needed
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter]
    search_fields = ['id', 'name', 'slug']  # Adjust the fields you want to search on

class ProductAPIView(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsSellerOrReadOnly]  # Add your permission classes here if needed
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'name', 'slug', 'description', 'seller__store_name', 'brand__name', 'brand__slug', 'category__name', 'category__slug']  # Adjust the fields you want to search on
    filterset_fields = ['seller','category', 'brand', 'is_active']  # Adjust the fields you want to filter on

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user.seller_account)
        
class ProductVariantAPIView(ModelViewSet):
    queryset = models.ProductVariant.objects.all()
    serializer_class = serializers.ProductVariantSerializer
    permission_classes = [IsSellerOrReadOnlyForProductData]  # Add your permission classes here if needed
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'sku', 'product__name', 'product__slug']  # Adjust the fields you want to search on
    filterset_fields = ['product', 'sku', 'regular_price' ,'price', 'stock', 'is_active']  # Adjust the fields you want to filter on

    def perform_create(self, serializer):
        serializer.save()  # You can add additional logic here if needed
        # For example, if you want to set the product automatically based on the request
        
class AttributeAPIView(ModelViewSet):
    queryset = models.Attribute.objects.all()
    serializer_class = serializers.AttributeSerializer
    permission_classes = [IsAdminOrReadOnly]  # Add your permission classes here if needed
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter]
    search_fields = ['id', 'name']  # Adjust the fields you want to search on

class AttributeValueAPIView(ModelViewSet):
    queryset = models.AttributeValue.objects.all()
    serializer_class = serializers.AttributeValueSerializer
    permission_classes = [IsAdminOrReadOnly]  # Add your permission classes here if needed
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'value', 'attribute__name']  # Adjust the fields you want to search
    filterset_fields = ['attribute']

class VariantAttributeValueAPIView(ModelViewSet):
    queryset = models.VariantAttributeValue.objects.all()
    serializer_class = serializers.VariantAttributeValueSerializer
    permission_classes = [IsSellerOrReadOnlyForVariantAttributeValue]  # Add your permission classes here if needed
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter]
    search_fields = ['id', 'value__value', 'value__attribute__name', 'variant__sku']  # Adjust the fields you want to search on

    def perform_create(self, serializer):
        serializer.save()  # You can add additional logic here if needed
        
class ProductImageAPIView(ModelViewSet):
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
    permission_classes = [IsSellerOrReadOnlyForProductData]  # Add your permission classes here if needed
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter]
    search_fields = ['id', 'image', 'alt_text']  # Adjust the fields you want to search

    def perform_create(self, serializer):
        serializer.save()  # You can add additional logic here if needed