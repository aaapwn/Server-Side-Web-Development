# Django Views

# Creating API handler function

View เป็นส่วน interface ที่ web application รับ request จาก client และ response กลับไป

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the index page of polls app")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

## Routing APIs to URLs

```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

หมายเหตุ: int:question_id เป็นการประกาศ path parameter ซึ่งจะรับค่าตัวแปรที่ถูกส่งมาใน url

# Rendering HTML via views

เรามาปรับแก้ไข view index() ให้ทำการ query ข้อมูล question 5 รายการล่าสุด เรียงตาม pub_date แบบจากมากไปน้อย

```python
from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)

# Leave the rest of the views (detail, results, vote) unchanged
```

ใน view index() เราได้ทำการ return list ของ questions ออกมา และส่งต่อข้อมูลไปยัง `/polls/index.html`

เราจะต้องไปสร้างไฟล์ **template** ก่อน โดยสร้าง folder `/polls/templates` และสร้างไฟล์ `/polls/templates/index.html` และเพิ่ม code ด้านล่าง

```html
<html>
    <head>
    </head>
    <body>
        <h1>Lastest questions</h1>
        {% if latest_question_list %}
            <ul>
            {% for question in latest_question_list %}
                <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No polls are available.</p>
        {% endif %}
    </body>
</html>
```

แก้ไขไฟล์ `mysite/settings.py` เพิ่ม code ดังนี้

```python
import os
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)
```

# Returning 404

```python
from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Question

...

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "detail.html", {"question": question})
```
