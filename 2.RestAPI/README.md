py -m venv .venv

.venv\Scripts\activate.bat

pip install django

python.exe -m pip install --upgrade pip

django-admin startproject storeapi

cd storeapi

py manage.py runserver 4096

py manage.py migrate

py manage.py startapp product

python manage.py makemigrations

python manage.py migrate

py manage.py createsuperuser

admin

Qwerty1-

py manage.py runserver 4096

pip install djangorestframework