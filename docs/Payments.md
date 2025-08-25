# Payments API Documentation

This document outlines the API endpoints for payment management in the Halum Hut platform.

## Payment Endpoints

### List Payments

Retrieves all payments for the authenticated user.

- **URL**: `/orders/api/payments/`
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
      "order": 1,
      "user": 1,
      "amount": "1598.00",
      "method": "COD",
      "status": "pending",
      "transaction_id": null,
      "created_at": "2023-01-15T14:30:00Z",
      "updated_at": "2023-01-15T14:30:00Z"
    },
    {
      "id": 2,
      "order": 2,
      "user": 1,
      "amount": "899.00",
      "method": "ONLINE",
      "status": "completed",
      "transaction_id": "txn_123456789",
      "created_at": "2023-01-20T10:15:00Z",
      "updated_at": "2023-01-20T10:20:00Z"
    }
  ]
}
```

### Retrieve Payment Detail

Retrieves a specific payment by ID.

- **URL**: `/orders/api/payments/{id}/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`

**Response**:

```json
{
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
```

### Create Online Payment

Initiates an online payment for an order.

- **URL**: `/orders/api/create-payment/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Headers**: `Authorization: Bearer <access_token>`

**Request Body**:

```json
{
  "order_id": 1,
  "payment_method": "ONLINE"
}
```

**Response**:

```json
{
  "payment_id": 3,
  "checkout_url": "https://payment-gateway.com/checkout/session_123456",
  "amount": "1598.00",
  "currency": "USD",
  "status": "pending"
}
```

### Payment Webhook

Endpoint for payment gateway to send payment status updates.

- **URL**: `/orders/api/payment-webhook/`
- **Method**: `POST`
- **Auth Required**: No (Uses webhook secret for verification)
- **Headers**: `X-Webhook-Signature: <signature>`

**Request Body** (example from payment gateway):

```json
{
  "event_type": "payment.completed",
  "payment_id": "txn_123456789",
  "order_reference": "1",
  "amount": "1598.00",
  "status": "completed",
  "timestamp": "2023-01-15T15:30:00Z"
}
```

**Response**:

```json
{
  "status": "success",
  "message": "Webhook processed successfully"
}
```

## Payment Status Values

Payments can have the following status values:

- `pending`: Payment has been initiated but not completed
- `processing`: Payment is being processed
- `completed`: Payment has been successfully completed
- `failed`: Payment has failed
- `refunded`: Payment has been refunded

## Payment Methods

The following payment methods are supported:

- `COD`: Cash On Delivery
- `ONLINE`: Online payment through integrated payment gateway

## Validation Rules

- Order must exist and belong to the authenticated user
- Order must not have an existing completed payment
- Payment amount must match the order total
- For online payments, the payment gateway must be properly configured
- Webhook requests must include a valid signature for verification