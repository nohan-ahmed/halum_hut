# Users API Documentation

This document outlines the API endpoints for user management in the Halum Hut platform, including authentication, registration, and profile management.

## Authentication Endpoints

### Register User

Creates a new user account and sends a verification email.

- **URL**: `/accounts/api/register/`
- **Method**: `POST`
- **Auth Required**: No
- **Rate Limit**: Yes (register scope)

**Request Body**:

```json
{
  "email": "user@example.com",
  "password1": "securepassword123",
  "password2": "securepassword123",
  "first_name": "John",
  "last_name": "Doe",
  "phone_number": "+1234567890",
  "date_of_birth": "1990-01-01",
  "gender": "M"
}
```

**Response**:

```json
{
  "message": "Please verify your email address."
}
```

**Status Codes**:
- `201 Created`: Registration successful, verification email sent
- `400 Bad Request`: Invalid input data

### Verify Email

Activates a user account using the verification link sent via email.

- **URL**: `/accounts/api/verify-email/<uidb64>/<token>/`
- **Method**: `GET`
- **Auth Required**: No
- **Rate Limit**: Yes (register scope)

**Response**:

```json
{
  "message": "Email verified successfully."
}
```

**Status Codes**:
- `200 OK`: Email verification successful
- `400 Bad Request`: Invalid verification link

### Login

Authenticates a user and returns JWT tokens.

- **URL**: `/accounts/api/login/`
- **Method**: `POST`
- **Auth Required**: No

**Request Body**:

```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Response**:

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Status Codes**:
- `200 OK`: Login successful
- `400 Bad Request`: Invalid credentials
- `401 Unauthorized`: Account not verified

### Refresh Token

Generates a new access token using a refresh token.

- **URL**: `/accounts/api/token/refresh/`
- **Method**: `POST`
- **Auth Required**: No

**Request Body**:

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Response**:

```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Status Codes**:
- `200 OK`: Token refresh successful
- `401 Unauthorized`: Invalid refresh token

### Google Login

Authenticates a user using Google OAuth2.

- **URL**: `/accounts/api/google/`
- **Method**: `POST`
- **Auth Required**: No

**Request Body**:

```json
{
  "access_token": "google_oauth2_access_token",
  "id_token": "google_oauth2_id_token"
}
```

**Response**:

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Status Codes**:
- `200 OK`: Login successful
- `400 Bad Request`: Invalid Google tokens

## User Address Management

### List User Addresses

Retrieves all addresses for the authenticated user.

- **URL**: `/accounts/api/addresses/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Rate Limit**: Yes (user rate throttle)

**Query Parameters**:
- `page`: Page number for pagination
- `page_size`: Number of results per page
- `search`: Search by country, city, or state
- `city`: Filter by city
- `state`: Filter by state

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
  ]
}
```

**Status Codes**:
- `200 OK`: Successful retrieval
- `401 Unauthorized`: Authentication required

### Create Address

Creates a new address for the authenticated user.

- **URL**: `/accounts/api/addresses/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Rate Limit**: Yes (user rate throttle)

**Request Body**:

```json
{
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

**Status Codes**:
- `201 Created`: Address created successfully
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Authentication required

### Retrieve Address

Retrieves a specific address by ID.

- **URL**: `/accounts/api/addresses/{id}/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Rate Limit**: Yes (user rate throttle)

**Response**:

```json
{
  "id": 1,
  "user": 1,
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

**Status Codes**:
- `200 OK`: Successful retrieval
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Not the owner of the address
- `404 Not Found`: Address not found

### Update Address

Updates an existing address.

- **URL**: `/accounts/api/addresses/{id}/`
- **Method**: `PUT`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Rate Limit**: Yes (user rate throttle)

**Request Body**:

```json
{
  "address_line_1": "456 New St",
  "address_line_2": "Suite 10",
  "city": "Boston",
  "state": "MA",
  "postal_code": "02108",
  "country": "USA",
  "is_default": true
}
```

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "address_line_1": "456 New St",
  "address_line_2": "Suite 10",
  "city": "Boston",
  "state": "MA",
  "postal_code": "02108",
  "country": "USA",
  "is_default": true,
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-02T12:00:00Z"
}
```

**Status Codes**:
- `200 OK`: Address updated successfully
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Not the owner of the address
- `404 Not Found`: Address not found

### Partial Update Address

Updates specific fields of an existing address.

- **URL**: `/accounts/api/addresses/{id}/`
- **Method**: `PATCH`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Rate Limit**: Yes (user rate throttle)

**Request Body**:

```json
{
  "city": "Chicago",
  "state": "IL"
}
```

**Response**:

```json
{
  "id": 1,
  "user": 1,
  "address_line_1": "456 New St",
  "address_line_2": "Suite 10",
  "city": "Chicago",
  "state": "IL",
  "postal_code": "02108",
  "country": "USA",
  "is_default": true,
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-03T12:00:00Z"
}
```

**Status Codes**:
- `200 OK`: Address updated successfully
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Not the owner of the address
- `404 Not Found`: Address not found

### Delete Address

Deletes an address.

- **URL**: `/accounts/api/addresses/{id}/`
- **Method**: `DELETE`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Rate Limit**: Yes (user rate throttle)

**Response**:
- No content

**Status Codes**:
- `204 No Content`: Address deleted successfully
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Not the owner of the address
- `404 Not Found`: Address not found

## Validation Rules

- Email must be unique and valid format
- Password must meet complexity requirements (typically 8+ characters with mix of letters, numbers, and symbols)
- Phone number must be in valid format
- Date of birth must be a valid date in the past
- Gender must be one of the allowed choices (typically 'M', 'F', 'O')
- Address fields have maximum length constraints (typically 255 characters)
- Postal code format validation depends on the country