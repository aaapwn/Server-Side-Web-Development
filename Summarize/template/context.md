# Context

Context คือการส่งค่าต่าง ๆ ที่เราได้เขียนใน `views.py` ส่งไป render ใน template ที่เราได้เตรียมไว้ เช่น

{% code title="views.py" %}
```python
# import render เพื่อใช้ render template django
from django.shortcuts import render
from shop.models import *

# ส่งข้อมูลของ Customer ทุกคนไปที่ Client
def showCustomer(request):
    # อยากส่งอะไรไปบ้าง เก็บใน dict เป็น key และ value
    context = {
        "first_name": "Puwit",
        "last_name": "Nunpan"
    }
    return render(request, "customer.html", context)
```
{% endcode %}

```html
{% raw %}
{% extends 'layout.html' %}

{% block title %}this is title{% endblock %}

{% block head %}
<h1>Hello, World!</h1>
{% endblock %}

{% block content %}
<!-- เมื่อต้องการแสดงค่า ให้นำชื่อ key มาใส่ใน {{ key }} -->
<p>{{ first_name }} {{ last_name }}</p>
{% endblock %}
{% endraw %}
```
