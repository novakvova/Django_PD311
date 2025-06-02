## Python Django

```
py --version
py -m venv .venv
.venv\Scripts\activate.bat

python.exe -m pip install --upgrade pip

py -m pip install Django
py
>>> import django
>>> print(django.get_version())
>>> exit

py -m django --version
mkdir djangotutorial

django-admin startproject mysite djangotutorial

cd djangotutorial

py manage.py runserver 4891

ctrl+c

py manage.py startapp polls

py manage.py runserver 4891

pip install psycopg2-binary

py manage.py migrate

py manage.py makemigrations polls

deactivate
```