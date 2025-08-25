# Notifications API Documentation

This document outlines the API endpoints for managing user notifications in the Halum Hut platform.

## Notification Endpoints

### List User Notifications

Retrieves all notifications for the authenticated user.

- **URL**: `/notifications/api/notifications/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Rate Limit**: Yes (user rate throttle)

**Query Parameters**:
- Standard pagination parameters
- `is_read` (optional): Filter by read status (true/false)

**Response**:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "notification_type": "order_status",
      "title": "Order Confirmed",
      "message": "Your order #12345 has been confirmed",
      "url": "/orders/12345/",
      "is_read": false,
      "created_at": "2023-01-01T12:00:00Z"
    },
    {
      "id": 2,
      "notification_type": "review",
      "title": "New Review",
      "message": "Someone reviewed a product you sell",
      "url": "/products/67890/reviews/",
      "is_read": true,
      "created_at": "2023-01-02T12:00:00Z"
    }
  ]
}
```

**Status Codes**:
- `200 OK`: Success
- `401 Unauthorized`: Authentication required

### Retrieve Notification Details

Retrieves details for a specific notification.

- **URL**: `/notifications/api/notifications/{id}/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Rate Limit**: Yes (user rate throttle)

**Response**:

```json
{
  "id": 1,
  "notification_type": "order_status",
  "title": "Order Confirmed",
  "message": "Your order #12345 has been confirmed",
  "url": "/orders/12345/",
  "metadata": {
    "order_id": 12345,
    "status": "confirmed"
  },
  "is_read": false,
  "created_at": "2023-01-01T12:00:00Z"
}
```

**Status Codes**:
- `200 OK`: Success
- `401 Unauthorized`: Authentication required
- `404 Not Found`: Notification not found or doesn't belong to user

### Mark Notification as Read

Marks a specific notification as read.

- **URL**: `/notifications/api/notifications/{id}/mark_read/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Rate Limit**: Yes (user rate throttle)

**Response**:

```json
{
  "id": 1,
  "notification_type": "order_status",
  "title": "Order Confirmed",
  "message": "Your order #12345 has been confirmed",
  "url": "/orders/12345/",
  "is_read": true,
  "created_at": "2023-01-01T12:00:00Z"
}
```

**Status Codes**:
- `200 OK`: Success
- `401 Unauthorized`: Authentication required
- `404 Not Found`: Notification not found or doesn't belong to user

### Mark All Notifications as Read

Marks all notifications for the authenticated user as read.

- **URL**: `/notifications/api/notifications/mark_all_read/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Rate Limit**: Yes (user rate throttle)

**Response**:

```json
{
  "message": "All notifications marked as read",
  "count": 5
}
```

**Status Codes**:
- `200 OK`: Success
- `401 Unauthorized`: Authentication required

## Notification Types

The platform supports various notification types:

| Type | Description |
|------|-------------|
| order_status | Updates about order status changes |
| payment | Payment-related notifications |
| review | New reviews on products |
| product_update | Updates about products (price changes, back in stock, etc.) |
| system | System announcements and updates |

## Real-time Notifications

In addition to REST API endpoints, the platform supports real-time notifications via WebSockets.

### WebSocket Connection

- **URL**: `/ws/notifications/{user_id}/`
- **Protocol**: WebSocket
- **Auth Required**: Yes (via token in query parameter)

**Connection Parameters**:
- `token`: JWT authentication token

**Message Format (received from server)**:

```json
{
  "type": "notification",
  "notification": {
    "id": 3,
    "notification_type": "order_status",
    "title": "Order Shipped",
    "message": "Your order #12345 has been shipped",
    "url": "/orders/12345/",
    "is_read": false,
    "created_at": "2023-01-03T14:30:00Z"
  }
}
```