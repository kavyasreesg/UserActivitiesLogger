release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: python manage.py dataloading

web: gunicorn user_activities.wsgi