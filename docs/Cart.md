# Cart API Documentation

This document outlines the API endpoints for shopping cart and wishlist management in the Halum Hut platform.

## Cart Management

### List User's Cart

Retrieves the authenticated user's shopping cart.

- **URL**: `/api/carts/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Owner only

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-10T15:30:00Z"
}
```

**Status Codes**:
- `200 OK`: Cart retrieved successfully
- `401 Unauthorized`: Not authenticated
- `404 Not Found`: Cart not found

### Create Cart

Creates a shopping cart for the authenticated user. A user can only have one cart.

- **URL**: `/api/carts/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Authenticated users

**Request Body**:

```json
{}
```

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-01T12:00:00Z"
}
```

**Status Codes**:
- `201 Created`: Cart created successfully
- `400 Bad Request`: User already has a cart
- `401 Unauthorized`: Not authenticated

## Cart Items Management

### List Cart Items

Retrieves all items in the authenticated user's cart.

- **URL**: `/api/cart-items/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Owner only
- **Pagination**: Yes

**Query Parameters**:
- `variant`: Filter by product variant ID
- `variant__product__name`: Filter by product name
- `search`: Search by SKU or product name

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "cart": 1,
      "variant": 5,
      "quantity": 2,
      "created_at": "2023-01-01T12:00:00Z",
      "updated_at": "2023-01-01T12:00:00Z"
    },
    {
      "id": 2,
      "cart": 1,
      "variant": 8,
      "quantity": 1,
      "created_at": "2023-01-02T14:30:00Z",
      "updated_at": "2023-01-02T14:30:00Z"
    }
  ]
}
```

**Status Codes**:
- `200 OK`: Cart items retrieved successfully
- `401 Unauthorized`: Not authenticated

### Add Item to Cart

Adds a product variant to the authenticated user's cart. If the user doesn't have a cart, one will be created automatically.

- **URL**: `/api/cart-items/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Authenticated users

**Request Body**:

```json
{
  "variant": 5,
  "quantity": 2
}
```

**Response**:

```json
{
  "id": 1,
  "cart": 1,
  "variant": 5,
  "quantity": 2,
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-01T12:00:00Z"
}
```

**Status Codes**:
- `201 Created`: Item added to cart successfully
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Not authenticated

### Update Cart Item

Updates the quantity of a product variant in the cart.

- **URL**: `/api/cart-items/<id>/`
- **Method**: `PUT`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Owner of the cart item

**Request Body**:

```json
{
  "variant": 5,
  "quantity": 3
}
```

**Response**:

```json
{
  "id": 1,
  "cart": 1,
  "variant": 5,
  "quantity": 3,
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-10T15:30:00Z"
}
```

**Status Codes**:
- `200 OK`: Cart item updated successfully
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: Not the owner of the cart item
- `404 Not Found`: Cart item not found

### Remove Cart Item

Removes a product variant from the cart.

- **URL**: `/api/cart-items/<id>/`
- **Method**: `DELETE`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Owner of the cart item

**Response**:

```
No content
```

**Status Codes**:
- `204 No Content`: Cart item removed successfully
- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: Not the owner of the cart item
- `404 Not Found`: Cart item not found

## Wishlist Management

### List User's Wishlists

Retrieves all wishlists belonging to the authenticated user.

- **URL**: `/api/wishlist/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Owner only
- **Pagination**: Yes

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "user": 1,
      "name": "Birthday Wishlist",
      "created_at": "2023-01-01T12:00:00Z",
      "updated_at": "2023-01-01T12:00:00Z"
    },
    {
      "id": 2,
      "user": 1,
      "name": "Holiday Wishlist",
      "created_at": "2023-01-02T14:30:00Z",
      "updated_at": "2023-01-02T14:30:00Z"
    }
  ]
}
```

**Status Codes**:
- `200 OK`: Wishlists retrieved successfully
- `401 Unauthorized`: Not authenticated

### Create Wishlist

Creates a new wishlist for the authenticated user.

- **URL**: `/api/wishlist/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Authenticated users

**Request Body**:

```json
{
  "name": "Birthday Wishlist"
}
```

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "name": "Birthday Wishlist",
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-01T12:00:00Z"
}
```

**Status Codes**:
- `201 Created`: Wishlist created successfully
- `400 Bad Request`: Invalid input data or duplicate wishlist name
- `401 Unauthorized`: Not authenticated

### Update Wishlist

Updates a wishlist's name.

- **URL**: `/api/wishlist/<id>/`
- **Method**: `PUT`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Owner of the wishlist

**Request Body**:

```json
{
  "name": "Updated Wishlist Name"
}
```

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "name": "Updated Wishlist Name",
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-10T15:30:00Z"
}
```

**Status Codes**:
- `200 OK`: Wishlist updated successfully
- `400 Bad Request`: Invalid input data or duplicate wishlist name
- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: Not the owner of the wishlist
- `404 Not Found`: Wishlist not found

### Delete Wishlist

Deletes a wishlist and all its items.

- **URL**: `/api/wishlist/<id>/`
- **Method**: `DELETE`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Owner of the wishlist

**Response**:

```
No content
```

**Status Codes**:
- `204 No Content`: Wishlist deleted successfully
- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: Not the owner of the wishlist
- `404 Not Found`: Wishlist not found

## Wishlist Items Management

### List Wishlist Items

Retrieves all items in the authenticated user's wishlists.

- **URL**: `/api/wishlist-items/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Owner only
- **Pagination**: Yes

**Query Parameters**:
- `wishlist__user`: Filter by user ID
- `product__name`: Filter by product name
- `search`: Search by product name

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "wishlist": 1,
      "product": 5,
      "created_at": "2023-01-01T12:00:00Z",
      "updated_at": "2023-01-01T12:00:00Z"
    },
    {
      "id": 2,
      "wishlist": 1,
      "product": 8,
      "created_at": "2023-01-02T14:30:00Z",
      "updated_at": "2023-01-02T14:30:00Z"
    }
  ]
}
```

**Status Codes**:
- `200 OK`: Wishlist items retrieved successfully
- `401 Unauthorized`: Not authenticated

### Add Item to Wishlist

Adds a product to a wishlist.

- **URL**: `/api/wishlist-items/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Owner of the wishlist

**Request Body**:

```json
{
  "wishlist": 1,
  "product": 5
}
```

**Response**:

```json
{
  "id": 1,
  "wishlist": 1,
  "product": 5,
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-01T12:00:00Z"
}
```

**Status Codes**:
- `201 Created`: Item added to wishlist successfully
- `400 Bad Request`: Invalid input data or product already in wishlist
- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: Not the owner of the wishlist

### Remove Wishlist Item

Removes a product from a wishlist.

- **URL**: `/api/wishlist-items/<id>/`
- **Method**: `DELETE`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Owner of the wishlist item

**Response**:

```
No content
```

**Status Codes**:
- `204 No Content`: Wishlist item removed successfully
- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: Not the owner of the wishlist item
- `404 Not Found`: Wishlist item not found

## Status Codes

- `200 OK`: Successful retrieval or update
- `201 Created`: Resource created successfully
- `204 No Content`: Resource deleted successfully
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Permission denied
- `404 Not Found`: Resource not found