from rest_framework import serializers
from .models import Review, ReviewImage

# Serializer for ReviewImage model
# Handles single image data for a review
class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ["id", "image", "uploaded_at"]  # Fields to include in API
        read_only_fields = ["id", "uploaded_at"]  # Cannot be changed by client

# Serializer for Review model
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Show username, not editable
    images = ReviewImageSerializer(
        many=True, required=False, read_only=True
    )  # Nested display of existing review images
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True,  # Only used for uploading, not returned in response
        required=False
    )

    class Meta:
        model = Review
        fields = [
            "id", "product", "user", "rating", "comment",
            "images", "uploaded_images", "created_at"
        ]
        read_only_fields = ["user", "product", "created_at"]  # Protected backend fields

    # Create new review with optional uploaded images
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])  # Extract images from input
        review = Review.objects.create(**validated_data)  # Create review
        for img in uploaded_images:
            review_image = ReviewImage.objects.create(image=img)  # Create ReviewImage instance
            review.images.add(review_image)  # Link image to review
        return review

    # Update existing review and optionally add new images
    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])  # Extract new images
        # Update rating and comment if provided
        instance.rating = validated_data.get("rating", instance.rating)
        instance.comment = validated_data.get("comment", instance.comment)
        instance.save()

        # Add new images to review
        for img in uploaded_images:
            review_image = ReviewImage.objects.create(image=img)
            instance.images.add(review_image)

        return instance
