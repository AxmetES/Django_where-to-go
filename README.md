### Interesting places
A project to highlight and describe interesting places on 
the map of Moscow.

### Get start
- Clone project from repository.
- Create virtual environment: ```python3 -m venv venv```.
- Activate: ```source venv/bin/activate```.
- And install requirements.txt: ```pip install -r requirements.txt```
- Create .env with this variables and input yours values:
```.env
STATIC_URL='****'
STATIC_ROOT='****'
SECRET_KEY ='****'
MEDIA_URL='****'
MEDIA_ROOT='****'
DEBUG=False
```
- Create DataBase: ```python manage.py migrate``` .
- Create superuser: ```python manage.py createsuperuser``` .
- Enter place information by admin site. ```http://127.0.0.1:8000/admin```.

### Run
In cmd ```python manage.py runserver```.

### Deploy example
Example site [http://yerkin.pythonanywhere.com/"](http://yerkin.pythonanywhere.com/), Deployed by "www.pythonanywhere.com".

### Motivation
The code is written for educational purposes - this is a lesson in Python and web development on the site [Devman](https://dvmn.org).