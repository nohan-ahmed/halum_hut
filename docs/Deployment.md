# Deployment Guide

This guide covers deploying Halum Hut to production environments.

## Prerequisites

- Python 3.8+
- PostgreSQL 12+
- Redis (for Celery and Channels)
- Nginx or similar web server
- Domain name (optional but recommended)
- SSL certificate (recommended for production)

## Deployment Options

### 1. Docker Deployment (Recommended)

The simplest way to deploy Halum Hut is using Docker and docker-compose.

1. Clone the repository on your server:
   ```bash
   git clone https://github.com/yourusername/halum_hut.git
   cd halum_hut
   ```

2. Create and configure environment variables:
   ```bash
   cp .example.env .env
   # Edit .env with production settings
   ```

   Important settings to configure:
   - `DEBUG=False`
   - `SECRET_KEY` (use a strong, unique value)
   - `ALLOWED_HOSTS` (your domain name)
   - Database credentials
   - Email settings

3. Build and start the containers:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

4. Run migrations and create a superuser:
   ```bash
   docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
   docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
   ```

5. Collect static files:
   ```bash
   docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input
   ```

### 2. Manual Deployment

For manual deployment on a VPS or dedicated server:

1. Set up a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   ```bash
   cp .example.env .env
   # Edit .env with production settings
   ```

4. Set up PostgreSQL:
   ```bash
   sudo -u postgres createdb halum_hut
   sudo -u postgres createuser -P halum_hut_user
   sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE halum_hut TO halum_hut_user;"
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Collect static files:
   ```bash
   python manage.py collectstatic --no-input
   ```

7. Set up Gunicorn as the WSGI server:
   Create a systemd service file `/etc/systemd/system/halum_hut.service`:
   ```
   [Unit]
   Description=Halum Hut Gunicorn daemon
   After=network.target

   [Service]
   User=www-data
   Group=www-data
   WorkingDirectory=/path/to/halum_hut
   ExecStart=/path/to/halum_hut/venv/bin/gunicorn --workers 3 --bind unix:/path/to/halum_hut/halum_hut.sock halum_hut.wsgi:application
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```

8. Set up Daphne for WebSocket support:
   Create a systemd service file `/etc/systemd/system/halum_hut_daphne.service`:
   ```
   [Unit]
   Description=Halum Hut Daphne daemon
   After=network.target

   [Service]
   User=www-data
   Group=www-data
   WorkingDirectory=/path/to/halum_hut
   ExecStart=/path/to/halum_hut/venv/bin/daphne -u /path/to/halum_hut/daphne.sock halum_hut.asgi:application
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```

9. Set up Celery for background tasks:
   Create a systemd service file `/etc/systemd/system/halum_hut_celery.service`:
   ```
   [Unit]
   Description=Halum Hut Celery Worker
   After=network.target

   [Service]
   User=www-data
   Group=www-data
   WorkingDirectory=/path/to/halum_hut
   ExecStart=/path/to/halum_hut/venv/bin/celery -A halum_hut worker -l info
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```

10. Configure Nginx:
    Create a configuration file `/etc/nginx/sites-available/halum_hut`:
    ```
    server {
        listen 80;
        server_name yourdomain.com;

        location = /favicon.ico { access_log off; log_not_found off; }
        
        location /static/ {
            root /path/to/halum_hut;
        }
        
        location /media/ {
            root /path/to/halum_hut;
        }
        
        location / {
            include proxy_params;
            proxy_pass http://unix:/path/to/halum_hut/halum_hut.sock;
        }
        
        location /ws/ {
            proxy_pass http://unix:/path/to/halum_hut/daphne.sock;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_redirect off;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Host $server_name;
        }
    }
    ```

11. Enable the site and restart services:
    ```bash
    sudo ln -s /etc/nginx/sites-available/halum_hut /etc/nginx/sites-enabled/
    sudo systemctl start halum_hut halum_hut_daphne halum_hut_celery
    sudo systemctl enable halum_hut halum_hut_daphne halum_hut_celery
    sudo systemctl restart nginx
    ```

12. Set up SSL with Let's Encrypt:
    ```bash
    sudo apt install certbot python3-certbot-nginx
    sudo certbot --nginx -d yourdomain.com
    ```

## Monitoring and Maintenance

### Logging

Configure logging in `settings.py` to write logs to files:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/path/to/logs/halum_hut.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}
```

### Backups

Set up regular database backups:

```bash
# Create a backup script
cat > /path/to/backup.sh << 'EOF'
#!/bin/bash
BACKUP_DIR="/path/to/backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
PGPASSWORD=your_password pg_dump -U halum_hut_user -h localhost halum_hut > "$BACKUP_DIR/halum_hut_$TIMESTAMP.sql"
tar -czf "$BACKUP_DIR/media_$TIMESTAMP.tar.gz" /path/to/halum_hut/media
find "$BACKUP_DIR" -name "*.sql" -mtime +7 -delete
find "$BACKUP_DIR" -name "*.tar.gz" -mtime +7 -delete
EOF

# Make it executable
chmod +x /path/to/backup.sh

# Add to crontab
echo "0 2 * * * /path/to/backup.sh" | crontab -
```

### Updates

To update the application:

```bash
# Pull latest changes
git pull

# Activate virtual environment
source venv/bin/activate

# Install any new dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input

# Restart services
sudo systemctl restart halum_hut halum_hut_daphne halum_hut_celery
```

## Troubleshooting

### Common Issues

1. **Static files not loading**
   - Check STATIC_ROOT and STATIC_URL settings
   - Ensure collectstatic has been run
   - Verify Nginx configuration for static files

2. **Database connection errors**
   - Verify database credentials in .env
   - Check if PostgreSQL service is running
   - Ensure database and user exist with proper permissions

3. **WebSocket connection failures**
   - Check Daphne service status
   - Verify Nginx WebSocket proxy configuration
   - Ensure Redis is running for channel layers

4. **500 Server Errors**
   - Check application logs for exceptions
   - Verify DEBUG=False in production
   - Check file permissions for media and static directories

For more assistance, please open an issue on GitHub.