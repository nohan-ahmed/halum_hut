# Products API Documentation

This document outlines the API endpoints for product management in the Halum Hut platform.

## Categories

### List Categories

Retrieves a list of all product categories.

- **URL**: `/products/api/categories/`
- **Method**: `GET`
- **Auth Required**: No
- **Permissions**: Anyone can view

**Query Parameters**:
- `search`: Search by name or slug

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Electronics",
      "description": "Electronic devices and accessories",
      "parent": null,
      "slug": "electronics",
      "thumbnail": "http://example.com/media/categories/electronics.jpg"
    },
    {
      "id": 2,
      "name": "Smartphones",
      "description": "Mobile phones and accessories",
      "parent": 1,
      "slug": "smartphones",
      "thumbnail": "http://example.com/media/categories/smartphones.jpg"
    }
  ]
}
```

### Create Category

Creates a new product category.

- **URL**: `/products/api/categories/`
- **Method**: `POST`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Admin only

**Request Body**:

```json
{
  "name": "Laptops",
  "description": "Notebook computers and accessories",
  "parent": 1,
  "thumbnail": "file_upload"
}
```

**Response**:

```json
{
  "id": 3,
  "name": "Laptops",
  "description": "Notebook computers and accessories",
  "parent": 1,
  "slug": "laptops",
  "thumbnail": "http://example.com/media/categories/laptops.jpg"
}
```

## Brands

### List Brands

Retrieves a list of all product brands.

- **URL**: `/products/api/brands/`
- **Method**: `GET`
- **Auth Required**: No
- **Permissions**: Anyone can view

**Query Parameters**:
- `search`: Search by name or slug

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Apple",
      "description": "Apple Inc.",
      "slug": "apple",
      "logo": "http://example.com/media/brands/apple.jpg"
    },
    {
      "id": 2,
      "name": "Samsung",
      "description": "Samsung Electronics",
      "slug": "samsung",
      "logo": "http://example.com/media/brands/samsung.jpg"
    }
  ]
}
```

### Create Brand

Creates a new product brand.

- **URL**: `/products/api/brands/`
- **Method**: `POST`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Admin only

**Request Body**:

```json
{
  "name": "Dell",
  "description": "Dell Technologies",
  "logo": "file_upload"
}
```

**Response**:

```json
{
  "id": 3,
  "name": "Dell",
  "description": "Dell Technologies",
  "slug": "dell",
  "logo": "http://example.com/media/brands/dell.jpg"
}
```

## Products

### List Products

Retrieves a list of all products.

- **URL**: `/products/api/products/`
- **Method**: `GET`
- **Auth Required**: No
- **Permissions**: Anyone can view

**Query Parameters**:
- `page`: Page number for pagination
- `page_size`: Number of results per page
- `search`: Search by name, slug, description, seller store name, brand name, or category name
- `category`: Filter by category ID
- `brand`: Filter by brand ID
- `seller`: Filter by seller ID
- `is_active`: Filter by active status (true/false)

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "iPhone 13",
      "description": "Apple iPhone 13 with A15 Bionic chip",
      "seller": 1,
      "brand": 1,
      "category": 2,
      "slug": "iphone-13",
      "thumbnail": "http://example.com/media/products/iphone13.jpg",
      "is_active": true,
      "created_at": "2023-01-01T12:00:00Z",
      "updated_at": "2023-01-10T15:30:00Z"
    }
  ]
}
```

### Create Product

Creates a new product.

- **URL**: `/products/api/products/`
- **Method**: `POST`
- **Auth Required**: Yes (Seller only)
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Seller only

**Request Body**:

```json
{
  "name": "Samsung Galaxy S22",
  "description": "Samsung Galaxy S22 with Snapdragon 8 Gen 1",
  "brand": 2,
  "category": 2,
  "thumbnail": "file_upload",
  "is_active": true
}
```

**Response**:

```json
{
  "id": 2,
  "name": "Samsung Galaxy S22",
  "description": "Samsung Galaxy S22 with Snapdragon 8 Gen 1",
  "seller": 1,
  "brand": 2,
  "category": 2,
  "slug": "samsung-galaxy-s22",
  "thumbnail": "http://example.com/media/products/samsung-galaxy-s22.jpg",
  "is_active": true,
  "created_at": "2023-01-15T12:00:00Z",
  "updated_at": "2023-01-15T12:00:00Z"
}
```

## Product Variants

### List Product Variants

Retrieves a list of all product variants.

- **URL**: `/products/api/product-variants/`
- **Method**: `GET`
- **Auth Required**: No
- **Permissions**: Anyone can view

**Query Parameters**:
- `product`: Filter by product ID
- `sku`: Filter by SKU
- `regular_price`: Filter by regular price
- `price`: Filter by current price
- `stock`: Filter by stock quantity
- `is_active`: Filter by active status (true/false)
- `search`: Search by SKU, product name, or product slug

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "product": 1,
      "sku": "IPHONE13-128-BLACK",
      "regular_price": "899.00",
      "price": "799.00",
      "stock": 50,
      "is_active": true,
      "created_at": "2023-01-01T12:00:00Z",
      "updated_at": "2023-01-10T15:30:00Z"
    },
    {
      "id": 2,
      "product": 1,
      "sku": "IPHONE13-256-BLACK",
      "regular_price": "999.00",
      "price": "899.00",
      "stock": 30,
      "is_active": true,
      "created_at": "2023-01-01T12:00:00Z",
      "updated_at": "2023-01-10T15:30:00Z"
    }
  ]
}
```

### Create Product Variant

Creates a new product variant.

- **URL**: `/products/api/product-variants/`
- **Method**: `POST`
- **Auth Required**: Yes (Seller only)
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Seller who owns the product

**Request Body**:

```json
{
  "product": 1,
  "sku": "IPHONE13-128-RED",
  "regular_price": "899.00",
  "price": "799.00",
  "stock": 25,
  "is_active": true
}
```

**Response**:

```json
{
  "id": 3,
  "product": 1,
  "sku": "IPHONE13-128-RED",
  "regular_price": "899.00",
  "price": "799.00",
  "stock": 25,
  "is_active": true,
  "created_at": "2023-01-15T12:00:00Z",
  "updated_at": "2023-01-15T12:00:00Z"
}
```

## Product Images

### List Product Images

Retrieves a list of all product images.

- **URL**: `/products/api/product-images/`
- **Method**: `GET`
- **Auth Required**: No
- **Permissions**: Anyone can view

**Query Parameters**:
- `search`: Search by image path or alt text

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "product": 1,
      "variant": 1,
      "image": "http://example.com/media/products/iphone13_black_1.jpg",
      "alt_text": "iPhone 13 Black Front View"
    },
    {
      "id": 2,
      "product": 1,
      "variant": 1,
      "image": "http://example.com/media/products/iphone13_black_2.jpg",
      "alt_text": "iPhone 13 Black Side View"
    }
  ]
}
```

### Add Product Image

Adds an image to a product or product variant.

- **URL**: `/products/api/product-images/`
- **Method**: `POST`
- **Auth Required**: Yes (Seller only)
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Seller who owns the product

**Request Body**:

```json
{
  "product": 1,
  "variant": 3,
  "image": "file_upload",
  "alt_text": "iPhone 13 Red Front View"
}
```

**Response**:

```json
{
  "id": 5,
  "product": 1,
  "variant": 3,
  "image": "http://example.com/media/products/iphone13_red_1.jpg",
  "alt_text": "iPhone 13 Red Front View"
}
```

## Attributes and Values

### List Attributes

Retrieves a list of all product attributes.

- **URL**: `/products/api/attributes/`
- **Method**: `GET`
- **Auth Required**: No
- **Permissions**: Anyone can view

**Query Parameters**:
- `search`: Search by name or ID

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Color"
    },
    {
      "id": 2,
      "name": "Storage"
    }
  ]
}
```

### Create Attribute

Creates a new product attribute.

- **URL**: `/products/api/attributes/`
- **Method**: `POST`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Admin only

**Request Body**:

```json
{
  "name": "Size"
}
```

**Response**:

```json
{
  "id": 3,
  "name": "Size"
}
```

### List Attribute Values

Retrieves a list of all attribute values.

- **URL**: `/products/api/attribute-values/`
- **Method**: `GET`
- **Auth Required**: No
- **Permissions**: Anyone can view

**Query Parameters**:
- `attribute`: Filter by attribute ID
- `search`: Search by value or attribute name

**Response**:

```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "attribute": 1,
      "value": "Black"
    },
    {
      "id": 2,
      "attribute": 1,
      "value": "Red"
    },
    {
      "id": 3,
      "attribute": 2,
      "value": "128GB"
    }
  ]
}
```

### Create Attribute Value

Creates a new attribute value.

- **URL**: `/products/api/attribute-values/`
- **Method**: `POST`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Admin only

**Request Body**:

```json
{
  "attribute": 1,
  "value": "Blue"
}
```

**Response**:

```json
{
  "id": 4,
  "attribute": 1,
  "value": "Blue"
}
```

### List Variant Attribute Values

Retrieves a list of all variant attribute value assignments.

- **URL**: `/products/api/variant-attribute-values/`
- **Method**: `GET`
- **Auth Required**: No
- **Permissions**: Anyone can view

**Query Parameters**:
- `search`: Search by value, attribute name, or variant SKU

**Response**:

```json
{
  "count": 4,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "variant": 1,
      "attribute": 1,
      "value": 1
    },
    {
      "id": 2,
      "variant": 1,
      "attribute": 2,
      "value": 3
    }
  ]
}
```

### Assign Attribute Value to Variant

Assigns an attribute value to a product variant.

- **URL**: `/products/api/variant-attribute-values/`
- **Method**: `POST`
- **Auth Required**: Yes (Seller only)
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Seller who owns the product variant

**Request Body**:

```json
{
  "variant": 3,
  "attribute": 1,
  "value": 2
}
```

**Response**:

```json
{
  "id": 5,
  "variant": 3,
  "attribute": 1,
  "value": 2
}
```

## Status Codes

- `200 OK`: Successful retrieval or update
- `201 Created`: Resource created successfully
- `204 No Content`: Resource deleted successfully
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Permission denied (not owner or admin)
- `404 Not Found`: Resource not found