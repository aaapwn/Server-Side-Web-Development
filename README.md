# Sheet cheat
```bash
mkdir server-side-sheet
cd server-side-sheet
git clone https://github.com/aaapwn/Server-Side-Web-Development.git aaapwn
git clone https://github.com/it-web-pro/django-week2.git aj-week2
git clone https://github.com/it-web-pro/django-week3.git aj-week3
git clone https://github.com/it-web-pro/django-week4.git aj-week4
git clone https://github.com/it-web-pro/django-week5.git aj-week5
git clone https://github.com/it-web-pro/django-week6.git aj-week6
git clone https://github.com/it-web-pro/django-week7.git aj-week7
git clone https://github.com/it-web-pro/django-week8.git aj-week8
code .
 

```


# Set up project
```bash
pip install virtualenv
# หากติด error
py -m pip install virtualenv
```
```bash
py -m venv myvenv
myvenv\Scripts\activate.bat
pip install django psycopg2
docker run --name my-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=12345678 -e POSTGRES_DB=postgres -p 5433:5432 -d postgres
django-admin startproject [project-name]
cd [project-name]
python manage.py startapp [app-name]
cd ..
code .
 
```

database:
- host: localhost
- port: 5433
- username: postgres
- password: 12345678
- database_name: postgres

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "12345678",
        "HOST": "localhost",
        "PORT": "5433",
    }
}
```
```python
import os

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)


STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

# optional for jupyter
```bash
pip install django-extensions ipython jupyter notebook   
pip install ipython==8.25.0 jupyter_server==2.14.1 jupyterlab==4.2.2 jupyterlab_server==2.27.2
pip install notebook==6.5.6
mkdir notebooks
```
- เพิ่ม extension ใน `settings.py`
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myapp",

    # เพิ่มอันนี้
    "django_extensions",
]
```
- ลากไฟล์ jupyter แปะใน folder notebooks
- รันคำสั่ง `python manage.py shell_plus --notebook`
