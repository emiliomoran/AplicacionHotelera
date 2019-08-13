# AplicacionHotelera

Después de haberlo clonado
/hotel

Para compilar:
- python manage.py makemigrations accesos
- python manage.py migrate accesos
- python manage.py migrate sessions
- python manage.py migrate social_django
- python manage.py runserver

Datos de la base:
/hotel/hotel/settings.py

...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "hotel",
        'USER': "postgres",
        'PASSWORD': "root",
        'HOST': "localhost",
        'PORT': "5432",
    }
}
...
