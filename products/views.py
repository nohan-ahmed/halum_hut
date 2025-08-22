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
    permission_classes = [IsAdminOrReadOnly] 
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter]
    search_fields = ['id', 'name', 'slug'] 
    

class CategoryAPIView(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAdminOrReadOnly]  
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter]
    search_fields = ['id', 'name', 'slug']  

class ProductAPIView(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsSellerOrReadOnly]  
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
    permission_classes = [IsSellerOrReadOnlyForProductData]  
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'sku', 'product__name', 'product__slug'] 
    filterset_fields = ['product', 'sku', 'regular_price' ,'price', 'stock', 'is_active'] 

    def perform_create(self, serializer):
        serializer.save()  # You can add additional logic here.(Polash:: 1/1/2023)

        
class AttributeAPIView(ModelViewSet):
    queryset = models.Attribute.objects.all()
    serializer_class = serializers.AttributeSerializer
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter]
    search_fields = ['id', 'name']  

class AttributeValueAPIView(ModelViewSet):
    queryset = models.AttributeValue.objects.all()
    serializer_class = serializers.AttributeValueSerializer
    permission_classes = [IsAdminOrReadOnly] 
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'value', 'attribute__name']  
    filterset_fields = ['attribute']

class VariantAttributeValueAPIView(ModelViewSet):
    queryset = models.VariantAttributeValue.objects.all()
    serializer_class = serializers.VariantAttributeValueSerializer
    permission_classes = [IsSellerOrReadOnlyForVariantAttributeValue]  
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter]
    search_fields = ['id', 'value__value', 'value__attribute__name', 'variant__sku']  

    def perform_create(self, serializer):
        serializer.save()  
        
class ProductImageAPIView(ModelViewSet):
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
    permission_classes = [IsSellerOrReadOnlyForProductData]  # Add your permission classes here if needed
    throttle_classes = [UserRateThrottle]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter]
    search_fields = ['id', 'image', 'alt_text'] 

    def perform_create(self, serializer):
        serializer.save()  