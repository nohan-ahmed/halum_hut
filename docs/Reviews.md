# Reviews API Documentation

This document outlines the API endpoints for managing product reviews in the Halum Hut platform.

## Review Endpoints

### List/Create Reviews for a Product

- **URL**: `/reviews/product/{product_id}/`
- **Methods**: `GET`, `POST`
- **Auth Required**: Yes (for POST), No (for GET)
- **Rate Limit**: Yes (user rate throttle)

#### GET - List Reviews for a Product

Retrieves all reviews for a specific product.

**Query Parameters**:
- Standard pagination parameters

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "user": "johndoe",
      "rating": 5,
      "comment": "Great product!",
      "images": [
        {
          "id": 1,
          "image": "/media/reviews/image1.jpg",
          "uploaded_at": "2023-01-01T12:00:00Z"
        }
      ],
      "created_at": "2023-01-01T12:00:00Z"
    },
    {
      "id": 2,
      "user": "janedoe",
      "rating": 4,
      "comment": "Good quality but a bit expensive",
      "images": [],
      "created_at": "2023-01-02T12:00:00Z"
    }
  ]
}
```

**Status Codes**:
- `200 OK`: Success

#### POST - Create a Review for a Product

Creates a new review for a specific product. A user can only review a product once.

**Request Body**:

```json
{
  "rating": 5,
  "comment": "Excellent product, highly recommended!",
  "uploaded_images": [
    {image_file_1},
    {image_file_2}
  ]
}
```

**Response**:

```json
{
  "id": 3,
  "user": "currentuser",
  "rating": 5,
  "comment": "Excellent product, highly recommended!",
  "images": [
    {
      "id": 3,
      "image": "/media/reviews/image3.jpg",
      "uploaded_at": "2023-01-03T12:00:00Z"
    },
    {
      "id": 4,
      "image": "/media/reviews/image4.jpg",
      "uploaded_at": "2023-01-03T12:00:00Z"
    }
  ],
  "created_at": "2023-01-03T12:00:00Z"
}
```

**Status Codes**:
- `201 Created`: Review created successfully
- `400 Bad Request`: Invalid input or user has already reviewed this product
- `401 Unauthorized`: Authentication required
- `404 Not Found`: Product not found

### Retrieve/Update/Delete a Review

- **URL**: `/reviews/{review_id}/`
- **Methods**: `GET`, `PUT`, `PATCH`, `DELETE`
- **Auth Required**: Yes (for PUT, PATCH, DELETE), No (for GET)
- **Rate Limit**: Yes (user rate throttle)
- **Permissions**: Owner only (for PUT, PATCH, DELETE)

#### GET - Retrieve a Review

Retrieves a specific review by ID.

**Response**:

```json
{
  "id": 1,
  "user": "johndoe",
  "product": 1,
  "rating": 5,
  "comment": "Great product!",
  "images": [
    {
      "id": 1,
      "image": "/media/reviews/image1.jpg",
      "uploaded_at": "2023-01-01T12:00:00Z"
    }
  ],
  "created_at": "2023-01-01T12:00:00Z"
}
```

**Status Codes**:
- `200 OK`: Success
- `404 Not Found`: Review not found

#### PUT/PATCH - Update a Review

Updates an existing review. Only the owner of the review can update it.

**Request Body**:

```json
{
  "rating": 4,
  "comment": "Updated: Good product but could be better",
  "uploaded_images": [
    {new_image_file}
  ]
}
```

**Response**:

```json
{
  "id": 1,
  "user": "johndoe",
  "product": 1,
  "rating": 4,
  "comment": "Updated: Good product but could be better",
  "images": [
    {
      "id": 1,
      "image": "/media/reviews/image1.jpg",
      "uploaded_at": "2023-01-01T12:00:00Z"
    },
    {
      "id": 5,
      "image": "/media/reviews/new_image.jpg",
      "uploaded_at": "2023-01-04T12:00:00Z"
    }
  ],
  "created_at": "2023-01-01T12:00:00Z"
}
```

**Status Codes**:
- `200 OK`: Review updated successfully
- `400 Bad Request`: Invalid input
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Not the owner of the review
- `404 Not Found`: Review not found

#### DELETE - Delete a Review

Deletes a specific review. Only the owner of the review can delete it.

**Status Codes**:
- `204 No Content`: Review deleted successfully
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Not the owner of the review
- `404 Not Found`: Review not found

## Data Models

### Review

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Unique identifier |
| user | User | User who created the review |
| product | Product | Product being reviewed |
| rating | Integer (1-5) | Star rating (1 to 5) |
| comment | Text | Review comment |
| images | Array of ReviewImage | Images attached to the review |
| created_at | DateTime | When the review was created |
| updated_at | DateTime | When the review was last updated |

### ReviewImage

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Unique identifier |
| image | File | Image file |
| uploaded_at | DateTime | When the image was uploaded |

## Validation Rules

1. A user can only review a product once
2. Rating must be between 1 and 5
3. Only the owner of a review can update or delete it