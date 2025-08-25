# Halum Hut

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.14+-red.svg)](https://www.django-rest-framework.org/)

Halum Hut is a comprehensive e-commerce platform built with Django and Django REST Framework. It provides a robust backend API for managing vendors, products, orders, payments, and user accounts.

## Features

- **User Authentication**: JWT-based authentication with email verification
- **Vendor Management**: Seller accounts, store profiles, and earnings tracking
- **Product Catalog**: Categories, brands, products with variants and attributes
- **Shopping Cart**: Cart management and wishlist functionality
- **Order Processing**: Order creation, tracking, and management
- **Payment Integration**: Support for Cash on Delivery (COD) with extensible payment methods
- **Notifications**: Real-time notifications using Django Channels and WebSockets
- **Reviews**: Product review and rating system

## Documentation

- [Getting Started Guide](docs/Getting_Started.md) - Setup instructions and environment configuration
- **API Documentation**:
  - [Accounts API](docs/Accounts.md) - User registration, authentication, and profile management
  - [Vendors API](docs/Vendors.md) - Seller account management and store operations
  - [Products API](docs/Products.md) - Product catalog, categories, and inventory management
  - [Cart API](docs/Cart.md) - Shopping cart and wishlist functionality
  - [Orders API](docs/Orders.md) - Order creation, processing, and tracking
  - [Payments API](docs/Payments.md) - Payment processing and transaction management
  - [Reviews API](docs/Reviews.md) - Product reviews and ratings
  - [Notifications API](docs/Notifications.md) - Real-time notification system
  - [Admin API](docs/Admin.md) - Administrative operations and dashboard
- [OpenAPI Specification](docs/halum-hut-api.yaml) - Complete API reference in OpenAPI 3.0 format

## Quick Example

```bash
# Authentication - Get JWT token
curl -X POST http://localhost:8000/accounts/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "yourpassword"}'

# Response
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}

# Get products
curl -X GET http://localhost:8000/products/api/products/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
```

## Project Structure
halum_hut/
├── accounts/          # User authentication and profile management
├── cart/              # Shopping cart and wishlist functionality
├── core/              # Core utilities and shared components
├── coupons/           # Discount coupons and promotions
├── docs/              # Documentation files
├── halum_hut/         # Project settings and configuration
├── inventory/         # Inventory management
├── notifications/     # Real-time notifications with WebSockets
├── orders/            # Order processing and management
├── products/          # Product catalog and management
├── reviews/           # Product reviews and ratings
├── vendors/           # Seller accounts and store management
├── .example.env       # Example environment variables
├── docker-compose.yml # Docker configuration
├── Dockerfile         # Docker build instructions
├── manage.py          # Django management script
└── requirements.txt   # Python dependencies


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/halum_hut.git
   cd halum_hut
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.example.env` to `.env` and configure environment variables:
   ```bash
   cp .example.env .env
   # Edit .env with your settings
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. For WebSocket support (notifications), run Daphne:
   ```bash
   daphne -p 8001 halum_hut.asgi:application
   ```

## Docker Deployment

For production deployment using Docker:

```bash
# Build and start containers
docker-compose up -d
# Create superuser
docker-compose exec web python manage.py createsuperuser
```

## Testing

Run the test suite:

```bash
python manage.py test
```

For coverage report:

```bash
coverage run --source='.' manage.py test
coverage report
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Security

If you discover any security related issues, please email security@example.com instead of using the issue tracker.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django and Django REST Framework communities
- All contributors who have helped shape this project