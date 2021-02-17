# UserActivitiesLogger<br />
This project implements an django application with User and ActivityPeriod models with custom management command to populate the database with some dummy data and design<br />
an API to serve that data in the json format using Django and Django Rest Framework.<br />
<br />
Detailed flow of the application:<br />
<br />
-> Created Project named user_activities and application named activity_logger.<br />
-> Created an URL in urls.py poniting to name 'activity_loggers' and mapped the URL to UserDataView which is an viewset.<br />
-> Created model named UserData containing fields name, place.<br />
-> Created model named ActivityData containing fields activity (which is foreign key to UserData model that represents many activities for a particular user), start_time,<br /> end_time <br />
and this model returns start_time and end_time in particular format when object is created.<br />
-> Created custom management command with its implementation under 'activity_logger/management/commands/dataloading.py' which creates dummy data for UserData and ActivityData 
models.<br />
<br />
Flow : When ever the URL is hit, the corresponding viewset is called that serializes(converts database data which is created using dummy data in dataloading.py to json format) 
and is displayed via viewset.<br />
<br />
<br />
Additional Notes:<br />
<br />
-> requirements.txt conatins below packages<br />
djangorestframework==3.11.0<br />
Django==3.0.7<br />
Pygments==2.6.1<br />
Markdown==3.2.1<br />
coreapi==2.3.3<br />
psycopg2-binary==2.8.4<br />
dj-database-url==0.5.0<br />
gunicorn==20.0.4<br />
whitenoise==5.0.1<br />
PyYAML==5.3.1<br />
django_heroku==0.3.1<br />
<br />
-> ProcFile is created to deploy in heroku which contains the following commands<br />
release: python manage.py makemigrations --no-input<br />
release: python manage.py migrate --no-input<br />
release: python manage.py dataloading<br />
web: gunicorn user_activities.wsgi<br />
<br />
-> Used default db.sqlite3 database.<br />
<br />
