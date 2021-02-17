# UserActivitiesLogger
This project implements an django application with User and ActivityPeriod models with custom management command to populate the database with some dummy data and design
an API to serve that data in the json format using Django and Django Rest Framework.

Detailed flow of the application:

-> Created Project named user_activities and application named activity_logger.
-> Created an URL in urls.py poniting to name 'activity_loggers' and mapped the URL to UserDataView which is an viewset.
-> Created model named UserData containing fields name, place.
-> Created model named ActivityData containing fields activity (which is foreign key to UserData model that represents many activities for a particular user), start_time, end_time 
and this model returns start_time and end_time in particular format when object is created.
-> Created custom management command with its implementation under 'activity_logger/management/commands/dataloading.py' which creates dummy data for UserData and ActivityData 
models.

Flow : When ever the URL is hit, the corresponding viewset is called that serializes(converts database data which is created using dummy data in dataloading.py to json format) 
and is displayed via viewset.


Additional Notes:

-> requirements.txt conatins below packages
djangorestframework==3.11.0
Django==3.0.7
Pygments==2.6.1
Markdown==3.2.1
coreapi==2.3.3
psycopg2-binary==2.8.4
dj-database-url==0.5.0
gunicorn==20.0.4
whitenoise==5.0.1
PyYAML==5.3.1
django_heroku==0.3.1

-> ProcFile is created to deploy in heroku which contains the following commands
release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: python manage.py dataloading
web: gunicorn user_activities.wsgi

-> Used default db.sqlite3 database.

