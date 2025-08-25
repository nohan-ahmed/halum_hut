# Vendors API Documentation

This document outlines the API endpoints for vendor management in the Halum Hut platform, including seller account creation and management.

## Seller Account Endpoints

### List Seller Accounts

Retrieves a list of all seller accounts.

- **URL**: `/vendors/api/seller-account/`
- **Method**: `GET`
- **Auth Required**: No (for reading)
- **Rate Limit**: Yes (user rate throttle)

**Query Parameters**:
- `page`: Page number for pagination
- `page_size`: Number of results per page
- `search`: Search by ID, store name, or store description
- `user`: Filter by user ID
- `store_name`: Filter by store name

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
      "store_name": "Fashion Hub",
      "store_description": "Latest fashion trends",
      "store_logo": "http://example.com/media/store_logos/fashion_hub.jpg",
      "contact_email": "fashion@example.com",
      "contact_phone": "+1234567890",
      "address": "123 Fashion St, New York",
      "balance": "1500.00",
      "total_earnings": "5000.00",
      "created_at": "2023-01-01T12:00:00Z",
      "updated_at": "2023-01-10T15:30:00Z"
    },
    {
      "id": 2,
      "user": 2,
      "store_name": "Tech Gadgets",
      "store_description": "Latest tech products",
      "store_logo": "http://example.com/media/store_logos/tech_gadgets.jpg",
      "contact_email": "tech@example.com",
      "contact_phone": "+0987654321",
      "address": "456 Tech Ave, San Francisco",
      "balance": "2500.00",
      "total_earnings": "7500.00",
      "created_at": "2023-01-05T10:00:00Z",
      "updated_at": "2023-01-12T09:45:00Z"
    }
  ]
}
```

**Status Codes**:
- `200 OK`: Successful retrieval

### Create Seller Account

Creates a new seller account for the authenticated user.

- **URL**: `/vendors/api/seller-account/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Rate Limit**: Yes (user rate throttle)

**Request Body**:

```json
{
  "store_name": "Fashion Hub",
  "store_description": "Latest fashion trends",
  "store_logo": "file_upload",
  "contact_email": "fashion@example.com",
  "contact_phone": "+1234567890",
  "address": "123 Fashion St, New York"
}
```

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "store_name": "Fashion Hub",
  "store_description": "Latest fashion trends",
  "store_logo": "http://example.com/media/store_logos/fashion_hub.jpg",
  "contact_email": "fashion@example.com",
  "contact_phone": "+1234567890",
  "address": "123 Fashion St, New York",
  "balance": "0.00",
  "total_earnings": "0.00",
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-01T12:00:00Z"
}
```

**Status Codes**:
- `201 Created`: Seller account created successfully
- `400 Bad Request`: Invalid input data or user already has a seller account
- `401 Unauthorized`: Authentication required

### Retrieve Seller Account

Retrieves a specific seller account by ID.

- **URL**: `/vendors/api/seller-account/{id}/`
- **Method**: `GET`
- **Auth Required**: No (for reading)
- **Rate Limit**: Yes (user rate throttle)

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "store_name": "Fashion Hub",
  "store_description": "Latest fashion trends",
  "store_logo": "http://example.com/media/store_logos/fashion_hub.jpg",
  "contact_email": "fashion@example.com",
  "contact_phone": "+1234567890",
  "address": "123 Fashion St, New York",
  "balance": "1500.00",
  "total_earnings": "5000.00",
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-10T15:30:00Z"
}
```

**Status Codes**:
- `200 OK`: Successful retrieval
- `404 Not Found`: Seller account not found

### Update Seller Account

Updates an existing seller account.

- **URL**: `/vendors/api/seller-account/{id}/`
- **Method**: `PUT`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Rate Limit**: Yes (user rate throttle)
- **Permissions**: Owner only

**Request Body**:

```json
{
  "store_name": "Fashion Hub Deluxe",
  "store_description": "Premium fashion trends",
  "store_logo": "file_upload",
  "contact_email": "premium@example.com",
  "contact_phone": "+1234567890",
  "address": "123 Fashion St, New York"
}
```

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "store_name": "Fashion Hub Deluxe",
  "store_description": "Premium fashion trends",
  "store_logo": "http://example.com/media/store_logos/fashion_hub_deluxe.jpg",
  "contact_email": "premium@example.com",
  "contact_phone": "+1234567890",
  "address": "123 Fashion St, New York",
  "balance": "1500.00",
  "total_earnings": "5000.00",
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-15T09:20:00Z"
}
```

**Status Codes**:
- `200 OK`: Seller account updated successfully
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Not the owner of the seller account
- `404 Not Found`: Seller account not found

### Partial Update Seller Account

Updates specific fields of an existing seller account.

- **URL**: `/vendors/api/seller-account/{id}/`
- **Method**: `PATCH`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Rate Limit**: Yes (user rate throttle)
- **Permissions**: Owner only

**Request Body**:

```json
{
  "store_description": "Premium fashion trends and accessories"
}
```

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "store_name": "Fashion Hub Deluxe",
  "store_description": "Premium fashion trends and accessories",
  "store_logo": "http://example.com/media/store_logos/fashion_hub_deluxe.jpg",
  "contact_email": "premium@example.com",
  "contact_phone": "+1234567890",
  "address": "123 Fashion St, New York",
  "balance": "1500.00",
  "total_earnings": "5000.00",
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-16T11:45:00Z"
}
```

**Status Codes**:
- `200 OK`: Seller account updated successfully
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Not the owner of the seller account
- `404 Not Found`: Seller account not found

### Delete Seller Account

Deletes a seller account.

- **URL**: `/vendors/api/seller-account/{id}/`
- **Method**: `DELETE`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Rate Limit**: Yes (user rate throttle)
- **Permissions**: Owner only

**Response**:
- No content

**Status Codes**:
- `204 No Content`: Seller account deleted successfully
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Not the owner of the seller account
- `404 Not Found`: Seller account not found

## Validation Rules

- Store name must be unique and between 3-100 characters
- Store description has a maximum length (typically 500 characters)
- Contact email must be a valid email format
- Contact phone must be in a valid phone number format
- Store logo must be an image file (JPEG, PNG, etc.) with size limitations
- A user can only have one seller account (enforced by the API)
- Balance and total earnings are read-only fields managed by the system