APP=mysql
python manage.py makemigrations $APP
python manage.py migration --database=$APP
APP=pgsql
python manage.py makemigrations $APP
python manage.py migration --database=$APP

# Start Django
python manage.py runserver 0.0.0.0:8000