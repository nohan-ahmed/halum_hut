# Halum Hut Architecture

This document provides an overview of the Halum Hut e-commerce platform architecture.

## System Architecture

Halum Hut follows a modern Django-based architecture with the following components:

─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  Client         │     │  Web Server     │     │  Application    │
│  (Browser/App)  │◄────┤  (Nginx)        │◄────┤  (Django/DRF)   │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
│
│
▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  WebSockets     │     │  Task Queue     │     │  Database       │
│  (Channels)     │     │  (Celery)       │     │  (PostgreSQL)   │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
│                       │
│                       │
▼                       ▼
┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │
│  Channel Layer  │     │  Cache          │
│  (Redis)        │     │  (Redis)        │
│                 │     │                 │
└─────────────────┘     └─────────────────┘



## Component Overview

### Frontend
- **Client Applications**: Web browsers and mobile apps that consume the API
- **Admin Interface**: Django admin site for backend management

### Backend Services
- **Web Server (Nginx)**: Handles HTTP requests, serves static files, and proxies to application servers
- **WSGI Application Server (Gunicorn)**: Runs the Django application for HTTP requests
- **ASGI Application Server (Daphne)**: Handles WebSocket connections for real-time features
- **Task Queue (Celery)**: Processes background tasks like sending emails and notifications
- **Message Broker (Redis)**: Facilitates communication between Celery workers and the application
- **Channel Layer (Redis)**: Enables WebSocket communication for real-time features
- **Cache (Redis)**: Stores frequently accessed data to improve performance
- **Database (PostgreSQL)**: Persistent data storage

## Application Structure

Halum Hut follows a modular architecture with Django apps representing different domains:

- **accounts**: User authentication, registration, and profile management
- **vendors**: Seller account management and store operations
- **products**: Product catalog, categories, and inventory management
- **cart**: Shopping cart and wishlist functionality
- **orders**: Order processing and management
- **payments**: Payment processing and transaction handling
- **reviews**: Product review and rating system
- **notifications**: Real-time notification system
- **core**: Shared utilities and base components

## Data Flow

### Authentication Flow
1. User submits credentials
2. Backend validates and issues JWT tokens
3. Client includes token in subsequent requests
4. Backend validates token for protected endpoints

### Order Processing Flow
1. User adds items to cart
2. User proceeds to checkout
3. Order is created in the database
4. Payment is processed
5. Order confirmation is sent
6. Seller is notified of new order
7. Order status is updated as it progresses

### Notification Flow
1. Event triggers notification (new order, message, etc.)
2. Celery task creates notification record
3. WebSocket message is sent to user's channel
4. Client receives and displays notification in real-time

## Security Considerations

- JWT-based authentication with short-lived access tokens
- HTTPS for all communications
- CSRF protection for form submissions
- Input validation and sanitization
- Permission-based access control
- Rate limiting to prevent abuse

## Scalability Considerations

- Stateless application servers for horizontal scaling
- Database connection pooling
- Caching frequently accessed data
- Asynchronous processing for time-consuming tasks
- Optimized database queries with proper indexing

## Future Architecture Enhancements

- Microservices architecture for specific components
- Content Delivery Network (CDN) for static assets
- Elasticsearch for improved search functionality
- Message queuing for inter-service communication
- Containerization and orchestration with Kubernetes