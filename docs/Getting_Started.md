# Getting Started with Halum Hut

This guide will help you set up and run the Halum Hut e-commerce backend on your local machine.

## Prerequisites

- Python 3.8+
- PostgreSQL
- Redis (for WebSocket support)
- Git

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/halum_hut.git
cd halum_hut
```

### 2. Set Up Python Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration

Copy the example environment file and configure it with your settings:

```bash
cp .example.env .env
```

Edit the `.env` file with your database credentials and other settings:

```
# Database settings
POSTGRES_DB=halum_hut
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Django settings
DEBUG=True
SECRET_KEY=your_secret_key

# Email settings (for user verification)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=your_email@gmail.com

# Google OAuth (for social login)
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

### 4. Database Setup

Ensure PostgreSQL is running, then create the database:

```bash
# Using psql
psql -U postgres
CREATE DATABASE halum_hut;
\q

# Run migrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Running the Development Server

```bash
python manage.py runserver
```

The API will be available at http://localhost:8000/

### 7. Running with Docker (Alternative)

If you prefer using Docker:

```bash
# Build and start containers
docker-compose up -d

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser
```

## Testing the API

### Using the Django Admin Interface

1. Navigate to http://localhost:8000/admin/
2. Log in with your superuser credentials
3. Browse and manage the database entities

### Using Postman

1. Import the Postman collection from the project repository (if available)
2. Or create a new request:
   - URL: http://localhost:8000/accounts/api/login/
   - Method: POST
   - Body (JSON):
     ```json
     {
       "email": "your_email@example.com",
       "password": "your_password"
     }
     ```
3. The response will contain access and refresh tokens for authentication

### Using cURL

```bash
# Authentication
curl -X POST http://localhost:8000/accounts/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "your_email@example.com", "password": "your_password"}'

# Using the token for authenticated requests
curl -X GET http://localhost:8000/products/api/products/ \
  -H "Authorization: Bearer your_access_token"
```

## API Authentication Flow

1. **Register a user account**:
   - Endpoint: `POST /accounts/api/register/`
   - The system will send a verification email

2. **Verify email**:
   - Click the link in the verification email or use the verification endpoint

3. **Login to get tokens**:
   - Endpoint: `POST /accounts/api/login/`
   - Store the access and refresh tokens

4. **Use the access token for API requests**:
   - Include in the Authorization header: `Bearer your_access_token`

5. **Refresh the token when it expires**:
   - Endpoint: `POST /accounts/api/token/refresh/`
   - Send the refresh token to get a new access token

## Common Issues and Troubleshooting

### Database Connection Issues

- Ensure PostgreSQL is running
- Verify database credentials in the `.env` file
- Check if the database exists

### Email Verification Not Working

- Check email settings in the `.env` file
- For Gmail, ensure you're using an App Password if 2FA is enabled
- Check spam folder for verification emails

### Redis Connection Issues

- Ensure Redis is running for WebSocket support
- Check Redis connection settings in `settings.py`

## Next Steps

- Explore the [API documentation](../README.md#documentation) for specific endpoints
- Set up a frontend application to interact with the API
- Create test data using the Django admin interface

For more detailed information about specific API endpoints, refer to the resource-specific documentation files.