# Started 
This repo is work from the following URL:

https://medium.com/swlh/jwt-auth-with-djangorest-api-9fb32b99b33c

some of the swagger-doc does not work 

we need to modify the following document

/Users/xiaofengzhu/devSource/Python/django-notes-api/venv/lib/python3.9/site-packages/rest_framework_swagger/templates/rest_framework_swagger/index.html

to change from [{% load staticfiles %}] to [{% load static %}]


# The new swagger configuration
Replace the django-rest-swagger with the following

https://github.com/axnsan12/drf-yasg#table-of-contents

# To run Django with Gunicorn

pip install uvicorn
pip install Gunicorn
pip install uvloop
pip install httptools

then edit the urls.py

--- When in development mode and when you are using some other server for local development add this to your url.py

--- from django.contrib.staticfiles.urls import staticfiles_urlpatterns

--- # ... the rest of your URLconf goes here ...

--- urlpatterns += staticfiles_urlpatterns()

gunicorn project.asgi:application -k uvicorn.workers.UvicornWorker       

