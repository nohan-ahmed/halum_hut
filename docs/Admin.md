# Admin API Documentation

This document outlines the API endpoints for admin operations in the Halum Hut platform.

## Admin Authentication

Admin endpoints require admin privileges. Users with the `is_staff` flag set to `true` have admin access.

- **Headers**: `Authorization: Bearer <admin_access_token>`

## User Management Endpoints

### List All Users

Retrieves a list of all users in the system.

- **URL**: `/admin/api/users/`
- **Method**: `GET`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <admin_access_token>`

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "email": "user@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "is_active": true,
      "is_staff": false,
      "date_joined": "2023-01-01T12:00:00Z",
      "last_login": "2023-01-15T08:30:00Z"
    },
    {
      "id": 2,
      "email": "admin@example.com",
      "first_name": "Admin",
      "last_name": "User",
      "is_active": true,
      "is_staff": true,
      "date_joined": "2022-12-01T10:00:00Z",
      "last_login": "2023-01-16T09:15:00Z"
    }
  ]
}
```

### Retrieve User Detail

Retrieves details for a specific user.

- **URL**: `/admin/api/users/{id}/`
- **Method**: `GET`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <admin_access_token>`

**Response**:

```json
{
  "id": 1,
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "is_active": true,
  "is_staff": false,
  "date_joined": "2023-01-01T12:00:00Z",
  "last_login": "2023-01-15T08:30:00Z",
  "addresses": [
    {
      "id": 1,
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
  ],
  "orders": [
    {
      "id": 1,
      "status": "pending",
      "total_price": "1598.00",
      "created_at": "2023-01-15T14:30:00Z"
    }
  ]
}
```

### Update User

Updates a user's information.

- **URL**: `/admin/api/users/{id}/`
- **Method**: `PUT`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <admin_access_token>`

**Request Body**:

```json
{
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Smith",
  "is_active": true,
  "is_staff": false
}
```

**Response**:

```json
{
  "id": 1,
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Smith",
  "is_active": true,
  "is_staff": false,
  "date_joined": "2023-01-01T12:00:00Z",
  "last_login": "2023-01-15T08:30:00Z"
}
```

### Delete User

Deactivates a user (soft delete).

- **URL**: `/admin/api/users/{id}/`
- **Method**: `DELETE`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <admin_access_token>`

**Response**:
- No content

## Order Management Endpoints

### List All Orders

Retrieves a list of all orders in the system.

- **URL**: `/admin/api/orders/`
- **Method**: `GET`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <admin_access_token>`

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "user": {
        "id": 1,
        "email": "user@example.com",
        "full_name": "John Doe"
      },
      "status": "pending",
      "total_price": "1598.00",
      "created_at": "2023-01-15T14:30:00Z",
      "payment_status": "pending"
    },
    {
      "id": 2,
      "user": {
        "id": 2,
        "email": "user2@example.com",
        "full_name": "Jane Smith"
      },
      "status": "delivered",
      "total_price": "899.00",
      "created_at": "2023-01-10T11:45:00Z",
      "payment_status": "completed"
    }
  ]
}
```

### Update Order Status

Updates the status of an order.

- **URL**: `/admin/api/orders/{id}/update-status/`
- **Method**: `PATCH`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <admin_access_token>`

**Request Body**:

```json
{
  "status": "processing"
}
```

**Response**:

```json
{
  "id": 1,
  "status": "processing",
  "updated_at": "2023-01-16T09:30:00Z"
}
```

## Vendor Management Endpoints

### List All Vendor Accounts

Retrieves a list of all vendor accounts.

- **URL**: `/admin/api/vendors/`
- **Method**: `GET`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <admin_access_token>`

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "user": {
        "id": 3,
        "email": "vendor1@example.com",
        "full_name": "Vendor One"
      },
      "business_name": "Tech Store",
      "business_address": "456 Commerce St, New York, NY 10001",
      "business_phone": "+1234567890",
      "business_email": "contact@techstore.com",
      "status": "approved",
      "created_at": "2023-01-05T10:00:00Z"
    },
    {
      "id": 2,
      "user": {
        "id": 4,
        "email": "vendor2@example.com",
        "full_name": "Vendor Two"
      },
      "business_name": "Fashion Outlet",
      "business_address": "789 Style Ave, Los Angeles, CA 90001",
      "business_phone": "+1987654321",
      "business_email": "info@fashionoutlet.com",
      "status": "pending",
      "created_at": "2023-01-12T14:20:00Z"
    }
  ]
}
```

### Update Vendor Status

Updates the status of a vendor account.

- **URL**: `/admin/api/vendors/{id}/update-status/`
- **Method**: `PATCH`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <admin_access_token>`

**Request Body**:

```json
{
  "status": "approved"
}
```

**Response**:

```json
{
  "id": 2,
  "status": "approved",
  "updated_at": "2023-01-16T10:15:00Z"
}
```

## Product Management Endpoints

### List All Products

Retrieves a list of all products in the system.

- **URL**: `/admin/api/products/`
- **Method**: `GET`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <admin_access_token>`

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
      "description": "Latest iPhone model with A15 Bionic chip",
      "brand": {
        "id": 1,
        "name": "Apple"
      },
      "category": {
        "id": 1,
        "name": "Smartphones"
      },
      "vendor": {
        "id": 1,
        "business_name": "Tech Store"
      },
      "is_active": true,
      "created_at": "2023-01-05T11:30:00Z"
    },
    {
      "id": 2,
      "name": "Samsung Galaxy S21",
      "description": "5G smartphone with 120Hz display",
      "brand": {
        "id": 2,
        "name": "Samsung"
      },
      "category": {
        "id": 1,
        "name": "Smartphones"
      },
      "vendor": {
        "id": 1,
        "business_name": "Tech Store"
      },
      "is_active": true,
      "created_at": "2023-01-06T09:45:00Z"
    }
  ]
}
```

### Update Product Status

Updates the active status of a product.

- **URL**: `/admin/api/products/{id}/update-status/`
- **Method**: `PATCH`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <admin_access_token>`

**Request Body**:

```json
{
  "is_active": false
}
```

**Response**:

```json
{
  "id": 1,
  "is_active": false,
  "updated_at": "2023-01-16T11:00:00Z"
}
```

## Dashboard Endpoints

### Get Dashboard Statistics

Retrieves statistics for the admin dashboard.

- **URL**: `/admin/api/dashboard/`
- **Method**: `GET`
- **Auth Required**: Yes (Admin only)
- **Headers**: `Authorization: Bearer <admin_access_token>`

**Response**:

```json
{
  "total_users": 150,
  "total_vendors": 25,
  "total_products": 500,
  "total_orders": 1200,
  "revenue": {
    "total": "125000.00",
    "this_month": "15000.00",
    "last_month": "12000.00"
  },
  "recent_orders": [
    {
      "id": 1201,
      "user": "user@example.com",
      "total_price": "1598.00",
      "status": "pending",
      "created_at": "2023-01-16T08:30:00Z"
    }
  ],
  "top_products": [
    {
      "id": 1,
      "name": "iPhone 13",
      "total_sales": 50,
      "revenue": "39950.00"
    }
  ]
}
```

## Validation Rules

- Only users with `is_staff=True` can access admin endpoints
- Order status can only be updated in a valid sequence (e.g., pending → processing → shipped → delivered)
- Vendor status can only be set to `pending`, `approved`, or `rejected`
- Products can only be deactivated, not deleted from the system