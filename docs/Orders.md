# Orders API Documentation

This document outlines the API endpoints for order management in the Halum Hut platform.

## Shipping Address Endpoints

### List Shipping Addresses

Retrieves all shipping addresses for the authenticated user.

- **URL**: `/orders/api/shipping-addresses/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`

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
      "full_name": "John Doe",
      "phone_number": "+1234567890",
      "address_line_1": "123 Main St",
      "address_line_2": "Apt 4B",
      "city": "New York",
      "state": "NY",
      "postal_code": "10001",
      "country": "USA",
      "is_default": true,
      "created_at": "2023-01-01T12:00:00Z",
      "updated_at": "2023-01-01T12:00:00Z"
    },
    {
      "id": 2,
      "user": 1,
      "full_name": "John Doe",
      "phone_number": "+1234567890",
      "address_line_1": "456 Work Ave",
      "address_line_2": "Suite 10",
      "city": "Boston",
      "state": "MA",
      "postal_code": "02108",
      "country": "USA",
      "is_default": false,
      "created_at": "2023-01-05T14:30:00Z",
      "updated_at": "2023-01-05T14:30:00Z"
    }
  ]
}
```

### Create Shipping Address

Creates a new shipping address for the authenticated user.

- **URL**: `/orders/api/shipping-addresses/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`

**Request Body**:

```json
{
  "full_name": "John Doe",
  "phone_number": "+1234567890",
  "address_line_1": "123 Main St",
  "address_line_2": "Apt 4B",
  "city": "New York",
  "state": "NY",
  "postal_code": "10001",
  "country": "USA",
  "is_default": true
}
```

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "full_name": "John Doe",
  "phone_number": "+1234567890",
  "address_line_1": "123 Main St",
  "address_line_2": "Apt 4B",
  "city": "New York",
  "state": "NY",
  "postal_code": "10001",
  "country": "USA",
  "is_default": true,
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-01T12:00:00Z"
}
```

### Retrieve Shipping Address

Retrieves a specific shipping address by ID.

- **URL**: `/orders/api/shipping-addresses/{id}/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "full_name": "John Doe",
  "phone_number": "+1234567890",
  "address_line_1": "123 Main St",
  "address_line_2": "Apt 4B",
  "city": "New York",
  "state": "NY",
  "postal_code": "10001",
  "country": "USA",
  "is_default": true,
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-01T12:00:00Z"
}
```

### Update Shipping Address

Updates an existing shipping address.

- **URL**: `/orders/api/shipping-addresses/{id}/`
- **Method**: `PUT`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`

**Request Body**:

```json
{
  "full_name": "John Doe",
  "phone_number": "+1234567890",
  "address_line_1": "789 New St",
  "address_line_2": "Unit 5",
  "city": "Chicago",
  "state": "IL",
  "postal_code": "60601",
  "country": "USA",
  "is_default": true
}
```

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "full_name": "John Doe",
  "phone_number": "+1234567890",
  "address_line_1": "789 New St",
  "address_line_2": "Unit 5",
  "city": "Chicago",
  "state": "IL",
  "postal_code": "60601",
  "country": "USA",
  "is_default": true,
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-10T09:15:00Z"
}
```

### Delete Shipping Address

Deletes a shipping address.

- **URL**: `/orders/api/shipping-addresses/{id}/`
- **Method**: `DELETE`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`

**Response**:
- No content

## Order Endpoints

### Create Cash On Delivery Order

Creates a new order with Cash On Delivery payment method.

- **URL**: `/orders/api/create-cod/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`

**Request Body**:

```json
{
  "shipping_address_id": 1,
  "notes": "Please deliver in the evening"
}
```

**Response**:

```json
{
  "order": {
    "id": 1,
    "user": 1,
    "shipping_address": 1,
    "status": "pending",
    "total_price": "1598.00",
    "notes": "Please deliver in the evening",
    "created_at": "2023-01-15T14:30:00Z",
    "updated_at": "2023-01-15T14:30:00Z"
  },
  "order_items": [
    {
      "id": 1,
      "order": 1,
      "product_variant": 1,
      "quantity": 2,
      "price": "799.00"
    }
  ],
  "payment": {
    "id": 1,
    "order": 1,
    "user": 1,
    "amount": "1598.00",
    "method": "COD",
    "status": "pending",
    "transaction_id": null,
    "created_at": "2023-01-15T14:30:00Z",
    "updated_at": "2023-01-15T14:30:00Z"
  }
}
```

### List Orders

Retrieves all orders for the authenticated user.

- **URL**: `/orders/api/order-list/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`

**Response**:

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "user": 1,
      "shipping_address": {
        "id": 1,
        "full_name": "John Doe",
        "phone_number": "+1234567890",
        "address_line_1": "123 Main St",
        "address_line_2": "Apt 4B",
        "city": "New York",
        "state": "NY",
        "postal_code": "10001",
        "country": "USA"
      },
      "status": "pending",
      "total_price": "1598.00",
      "notes": "Please deliver in the evening",
      "created_at": "2023-01-15T14:30:00Z",
      "updated_at": "2023-01-15T14:30:00Z",
      "items": [
        {
          "id": 1,
          "product_variant": {
            "id": 1,
            "product": {
              "id": 1,
              "name": "iPhone 13",
              "brand": {
                "id": 1,
                "name": "Apple"
              }
            },
            "sku": "IPHONE13-128-BLACK",
            "price": "799.00",
            "attributes": [
              {
                "attribute": "Storage",
                "value": "128GB"
              },
              {
                "attribute": "Color",
                "value": "Black"
              }
            ],
            "images": [
              "http://example.com/media/products/iphone13_black_1.jpg"
            ]
          },
          "quantity": 2,
          "price": "799.00"
        }
      ],
      "payment": {
        "id": 1,
        "method": "COD",
        "status": "pending",
        "amount": "1598.00",
        "transaction_id": null,
        "created_at": "2023-01-15T14:30:00Z"
      }
    }
  ]
}
```

### Retrieve Order Detail

Retrieves a specific order by ID.

- **URL**: `/orders/api/order-detail/{id}/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "shipping_address": {
    "id": 1,
    "full_name": "John Doe",
    "phone_number": "+1234567890",
    "address_line_1": "123 Main St",
    "address_line_2": "Apt 4B",
    "city": "New York",
    "state": "NY",
    "postal_code": "10001",
    "country": "USA"
  },
  "status": "pending",
  "total_price": "1598.00",
  "notes": "Please deliver in the evening",
  "created_at": "2023-01-15T14:30:00Z",
  "updated_at": "2023-01-15T14:30:00Z",
  "items": [
    {
      "id": 1,
      "product_variant": {
        "id": 1,
        "product": {
          "id": 1,
          "name": "iPhone 13",
          "brand": {
            "id": 1,
            "name": "Apple"
          }
        },
        "sku": "IPHONE13-128-BLACK",
        "price": "799.00",
        "attributes": [
          {
            "attribute": "Storage",
            "value": "128GB"
          },
          {
            "attribute": "Color",
            "value": "Black"
          }
        ],
        "images": [
          "http://example.com/media/products/iphone13_black_1.jpg"
        ]
      },
      "quantity": 2,
      "price": "799.00"
    }
  ],
  "payment": {
    "id": 1,
    "method": "COD",
    "status": "pending",
    "amount": "1598.00",
    "transaction_id": null,
    "created_at": "2023-01-15T14:30:00Z"
  }
}
```

## Order Status Values

Orders can have the following status values:

- `pending`: Order has been placed but not yet processed
- `processing`: Order is being processed
- `shipped`: Order has been shipped
- `delivered`: Order has been delivered
- `cancelled`: Order has been cancelled

## Validation Rules

- Shipping address must belong to the authenticated user
- User must have items in their cart to create an order
- Product variants must have sufficient stock for the order
- Order status transitions must follow a valid flow (e.g., cannot go from `cancelled` to `delivered`)