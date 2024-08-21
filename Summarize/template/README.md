# Template

## Django Template

Django template คือส่วนที่ใช้สำหรับสร้าง HTML หน้าเว็บ ซึ่งช่วยให้เราสามารถแสดงข้อมูลที่ส่งมาจาก Views และจัดการกับการแสดงผลหน้าตาของเว็บไซต์ได้อย่างง่ายดาย โดยใช้โครงสร้างแบบ HTML ร่วมกับ template language ของ Django

***

## Setup templates folder

ในแต่ละ app จะมี folder template เพื่อใช้เก็บไฟล์ html template ต่าง ๆ ที่จะนำไปใช้ render เพื่อแสดงไปยังหน้าเว็บแต่จะต้อง setup template ก่อนถึงจะใช้งานได้

1. สร้าง folder `templates` ไว้ใน folder app
2. เพิ่ม Code เหล่านี้ใน `settings.py`

{% code title="/myproject/settings.py" %}
```python
import os
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)
```
{% endcode %}

{% hint style="info" %}
เพิ่ม Code ใน `settings.py` เฉพาะครั้งแรกเท่านั้น หาก setup ใน project อื่นไม่ต้องเพิ่มแล้ว
{% endhint %}

***

## Render HTML on your website

สร้างไฟล์ html และเขียน website ตามปกติ หลังจากนั้นก็นำมา render ที่ `views.py()`&#x20;

```python
# import render เพื่อใช้ render template django
from django.shortcuts import render
from shop.models import *
import json

# ส่งข้อมูลของ Customer ทุกคนไปที่ Client
def showCustomer(request):
    cus = Customer.objects.all().values()
    return render(request, "customer.html")
```

ใช้ function `render()` โดย function นี้จะมี arguments หลัก ๆ คือ

* `request` คือ HTTPRequest โดยสามารถใส่ parameter `request` ของ function ที่เราได้เขียนไว้ได้เลย
* `template_name` คือ ชื่อ template ที่เราต้องการใช้ render โดยในตัวอย่างคือ `customer.html`
* `context` (optional) คือชุดข้อมูลที่ต้องการจะส่งไป render บน template
