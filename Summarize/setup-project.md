# Setup Project

System Requirements:

* [**Python 3**](https://www.python.org)  or later.
* [**Virtual Environment**](https://virtualenv.pypa.io/en/latest/installation.html)

***

## Setup Virtual Environment

* **สำหรับ Windows User**
  * สร้าง Virtual environment โดยการใช้ `py -m venv [env-name]`
  * Activate virtual environment ด้วยการใช้  `[env-name]\Scripts\activate.bat`

{% code title="terminal" %}
```bash
# Create a virtual environment
> py -m venv myvenv

# Activate virtual environment
> myvenv\Scripts\activate.bat
```
{% endcode %}

* **สำหรับ Mac/Linux User**
  * สร้าง Virtual environment โดยการใช้ `python -m venv [env-name]`
  * Activate virtual environment ด้วยการใช้  `source [env-name]/bin/activate`

{% code title="terminal" %}
```bash
# Create a virtual environment
> python -m venv myvenv

# Activate virtual environment
> source myvenv/bin/activate
```
{% endcode %}

{% hint style="danger" %}
เมื่อต้องการจะทำ Project ต่อ ต้อง Activate virtual environment ทุกครั้ง !!!
{% endhint %}

***

## Setup Django Project

* install django ด้วยคำสั่ง `pip install django`
* สร้าง Project ด้วยคำสั่ง `django-admin startproject [project-name]`

{% code title="terminal" %}
```bash
# install django
> pip install django

# create project
> django-admin startproject myproject

# enter the project folder
> cd myproject

# make sure manage.py is in the current directory
> ls
manage.py* myproject/

# start server
> python manage.py runserver
```
{% endcode %}

{% hint style="danger" %}
เมื่อต้องการจะใช้คำสั่งที่มี manage.py ต้อง make sure ว่ามีไฟล์ manage.py อยู่ใน current directory ทุกครั้ง !!!
{% endhint %}

***

## Create App

* create app ด้วยคำสั่ง `python manage.py startapp [app-name]`

{% code title="terminal" %}
```bash
python manage.py startapp myapp
```
{% endcode %}

* เพิ่ม app ที่เพิ่งสร้างใน `setting.py`

<pre class="language-python" data-title="/myproject/settings.py"><code class="lang-python">...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # add your app here
    <a data-footnote-ref href="#user-content-fn-1">'myapp',</a>
]

...
</code></pre>

{% hint style="info" %}
1 Project สามารถมีได้หลาย ๆ APPS
{% endhint %}

[^1]: add this
