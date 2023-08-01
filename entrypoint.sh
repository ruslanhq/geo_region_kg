#!/bin/sh

# wait for DB to start
sleep 60

# Perform database migrations
echo "Performing database migrations..."
python manage.py migrate

# Create superuser
echo "Creating superuser..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Create data
echo "Populate database..."
python manage.py populate_db

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:1111
