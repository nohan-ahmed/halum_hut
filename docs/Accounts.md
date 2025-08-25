# Accounts API Documentation

This document outlines the API endpoints for user account management in the Halum Hut platform, including authentication, registration, profile management, and address management.

## Authentication Endpoints

### Register User

Creates a new user account and sends a verification email.

- **URL**: `/accounts/api/registration/`
- **Method**: `POST`
- **Auth Required**: No
- **Rate Limit**: Yes (register scope)
- **Permissions**: Anyone can access

**Request Body**:

```json
{
  "username": "johndoe",
  "first_name": "John",
  "last_name": "Doe",
  "gender": "male",
  "email": "user@example.com",
  "password": "securepassword123",
  "confirm_password": "securepassword123"
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
- **Permissions**: Anyone can access

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
- **Permissions**: Anyone can access

**Request Body**:

```json
{
  "username": "johndoe",
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

### Logout

Invalidates the user's refresh token.

- **URL**: `/accounts/api/logout/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Authenticated users

**Request Body**:

```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Response**:

```json
{
  "detail": "Successfully logged out."
}
```

**Status Codes**:
- `200 OK`: Logout successful
- `401 Unauthorized`: Invalid token

### Password Reset

Sends a password reset email to the user.

- **URL**: `/accounts/api/password/reset/`
- **Method**: `POST`
- **Auth Required**: No
- **Permissions**: Anyone can access

**Request Body**:

```json
{
  "email": "user@example.com"
}
```

**Response**:

```json
{
  "detail": "Password reset e-mail has been sent."
}
```

**Status Codes**:
- `200 OK`: Password reset email sent
- `400 Bad Request`: Invalid email

### Password Reset Confirm

Resets the user's password using the token from the email.

- **URL**: `/accounts/api/password/reset/confirm/<uidb64>/<token>/`
- **Method**: `POST`
- **Auth Required**: No
- **Permissions**: Anyone with valid token

**Request Body**:

```json
{
  "new_password1": "newsecurepassword123",
  "new_password2": "newsecurepassword123"
}
```

**Response**:

```json
{
  "detail": "Password has been reset with the new password."
}
```

**Status Codes**:
- `200 OK`: Password reset successful
- `400 Bad Request`: Invalid input or token

### Google Login

Authenticates a user using Google OAuth.

- **URL**: `/accounts/api/google/`
- **Method**: `POST`
- **Auth Required**: No
- **Permissions**: Anyone can access

**Request Body**:

```json
{
  "access_token": "google-oauth-access-token"
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
- `400 Bad Request`: Invalid token

## User Profile Management

### Get User Profile

Retrieves the authenticated user's profile information.

- **URL**: `/accounts/api/user/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Authenticated users

**Response**:

```json
{
  "id": 1,
  "username": "johndoe",
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "profile_picture": "http://example.com/media/profile_pictures/johndoe.jpg",
  "phone_number": "+1234567890",
  "date_of_birth": "1990-01-01",
  "gender": "male",
  "bio": "Software developer based in New York"
}
```

**Status Codes**:
- `200 OK`: Profile retrieved successfully
- `401 Unauthorized`: Not authenticated

### Update User Profile

Updates the authenticated user's profile information.

- **URL**: `/accounts/api/user/`
- **Method**: `PUT`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Authenticated users

**Request Body**:

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "profile_picture": "file_upload",
  "phone_number": "+1234567890",
  "date_of_birth": "1990-01-01",
  "gender": "male",
  "bio": "Software developer based in New York"
}
```

**Response**:

```json
{
  "id": 1,
  "username": "johndoe",
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "profile_picture": "http://example.com/media/profile_pictures/johndoe.jpg",
  "phone_number": "+1234567890",
  "date_of_birth": "1990-01-01",
  "gender": "male",
  "bio": "Software developer based in New York"
}
```

**Status Codes**:
- `200 OK`: Profile updated successfully
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Not authenticated

## Address Management

### List User Addresses

Retrieves the authenticated user's address.

- **URL**: `/accounts/api/profile/address/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Authenticated users
- **Pagination**: Yes

**Query Parameters**:
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
      "city": "New York",
      "state": "NY",
      "postal_code": "10001",
      "country": "US",
      "created_at": "2023-01-01T12:00:00Z",
      "updated_at": "2023-01-10T15:30:00Z"
    }
  ]
}
```

**Status Codes**:
- `200 OK`: Address retrieved successfully
- `401 Unauthorized`: Not authenticated

### Create User Address

Creates an address for the authenticated user.

- **URL**: `/accounts/api/profile/address/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Authenticated users

**Request Body**:

```json
{
  "street": "123 Main St",
  "city": "New York",
  "state": "NY",
  "postal_code": "10001",
  "country": "US"
}
```

**Response**:

```json
{
  "id": 1,
  "city": "New York",
  "state": "NY",
  "postal_code": "10001",
  "country": "US",
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-01T12:00:00Z"
}
```

**Status Codes**:
- `201 Created`: Address created successfully
- `400 Bad Request`: Invalid input data or user already has an address
- `401 Unauthorized`: Not authenticated

### Update User Address

Updates the authenticated user's address.

- **URL**: `/accounts/api/profile/address/<id>/`
- **Method**: `PUT`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Owner of the address

**Request Body**:

```json
{
  "street": "456 Park Ave",
  "city": "New York",
  "state": "NY",
  "postal_code": "10022",
  "country": "US"
}
```

**Response**:

```json
{
  "id": 1,
  "city": "New York",
  "state": "NY",
  "postal_code": "10022",
  "country": "US",
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-15T09:45:00Z"
}
```

**Status Codes**:
- `200 OK`: Address updated successfully
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: Not the owner of the address
- `404 Not Found`: Address not found

### Delete User Address

Deletes the authenticated user's address.

- **URL**: `/accounts/api/profile/address/<id>/`
- **Method**: `DELETE`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`
- **Permissions**: Owner of the address

**Response**:

```
No content
```

**Status Codes**:
- `204 No Content`: Address deleted successfully
- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: Not the owner of the address
- `404 Not Found`: Address not found

## Status Codes

- `200 OK`: Successful retrieval or update
- `201 Created`: Resource created successfully
- `204 No Content`: Resource deleted successfully
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Permission denied
- `404 Not Found`: Resource not found