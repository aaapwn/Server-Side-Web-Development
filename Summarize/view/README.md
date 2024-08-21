# View

## Django Views

Django View คือส่วนที่จัดการกับการร้องขอ (request) และการตอบกลับ (response) ระหว่างผู้ใช้กับเว็บเซิร์ฟเวอร์ โดย Views จะทำหน้าที่ในการประมวลผลข้อมูลที่ได้รับจากผู้ใช้ (เช่นข้อมูลจากแบบฟอร์ม) และส่งกลับข้อมูลหรือ HTML หน้าเว็บให้กับผู้ใช้ หรือก็คือเป็นตัวประมวลของของหลังบ้านนั่นเอง

***

## Write view in your app&#x20;

1. เขียน logic ใน view ของ app ที่ต้องการ

{% code title="/myapp/views.py" %}
```python
# import HttpResponse เพื่อใช้การส่ง response กลับไปหา Client
from django.http import HttpResponse
# import model มาเพื่อใช้ทำ Query
from myapp.models import *
import json

# ส่งข้อมูลของ Customer ทุกคนไปที่ Client
def showCustomer(request):
    cus = Customer.objects.all().values()
    return HttpResponse(json.dumps(list(cus)), content_type="application/json")
```
{% endcode %}

2. สร้าง url path ของเว็บไซต์ โดยทำการสร้างไฟล์ `urls.py` ใน filder app ที่ต้องการ
3. เขียน url path ในไฟล์ `urls.py`

<pre class="language-python" data-title="/myapp/urls.py"><code class="lang-python"># import path เพื่อใช้การสร้าง url path ใหม่
from django.urls import path
# import views มาเพื่อใช้ function ที่เขียนไว้ในข้อ 1
<strong>from . import views
</strong>
urlpatterns = [
    path('showCustomer/', views.showCustomer, name='showCustomer'),
]
</code></pre>

โดย function `path()` จะเป็น function ที่ใช้เพื่อสร้าง path ใหม่ที่ใช้ในเว็บไซต์ โดยจะรับ arguments หลัก ๆ 3 ตัวที่ใช้บ่อย ๆ คือ

* `route` จะเป็น path ใหม่ที่เราต้องการ เช่น `about/`, `home/` โดยจะต้องไม่ขึ้นต้นด้วย `/` และลงท้ายด้วย `/`
* `view` จะเป็น function ที่ได้เขียนในไฟล์ views เช่น `views.showCustomer` คือ function showCustomer ที่ได้เขียนในไฟล์ `views.py`
* `name` (optional) จะเป็นชื่อของ path สามารถเอาไปใช้กับ function ต่าง ๆ ใน Django ได้ โดยจะไม่ต้องใส่ชื่อ path  เต็ม ๆ แต่เราสามารถใช้ชื่อที่ตั้งใน argument ตัวนี้ได้

***

## Add all path in your app to Project

จากหัวข้อที่แล้ว เราได้สร้าง view และเขียน path ใน app ไปแล้ว แต่ตอนนี้เรายังไม่สามารถเข้าถึงได้ผ่านเว็บไซต์ เราต้องนำ path ที่เขียนใน app มา apply ใน project ก่อน

{% code title="/myproject/urls.py" %}
```python
from django.contrib import admin
# import include เพิ่อนำมาใช้เพิ่ม url ที่เราสร้างใน app
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # include คือการเพิ่ม path ทั้งหมดที่เขียนใน app มาอยู่ใน project
    path('app/', include('myapp.urls')),
]
```
{% endcode %}

โดยตามตัวอย่าง คือ เราเพิ่ม path ทั้งหมดที่อยู่ใน myapp ให้มาอยู่ใน project โดยตามตัวอย่างหากเราต้องการเข้าถึงหน้า  showCustomer เราต้องไปที่ path `/app/showCustomer`&#x20;

#### ลองเทสที่เราเขียนกัน

1. run server โดยการใช้คำสั่ง `python manage.py runserver`
2. ใน browser ไปที่ localhost:8000/app/showCustomer

***

## HTTP Methods

* **GET** คือการดึงข้อมูลจากเซิร์ฟเวอร์ เช่น ดูหน้าเว็บโดยการพิมพ์ URL
* **POST** คือการส่งข้อมูลไปยังเซิร์ฟเวอร์เพื่อสร้างข้อมูลใหม่ เช่น การส่งฟอร์มสมัครสมาชิก
* **PUT** คือการอัปเดตข้อมูลที่มีอยู่บนเซิร์ฟเวอร์ เช่น การแก้ไขโปรไฟล์ผู้ใช้
* **DELETE** คือการลบข้อมูลจากเซิร์ฟเวอร์ เช่น การลบโพสต์ในระบบ

โดย url แต่ละตัว ต่อให้มันจะเหมือนกัน แต่ถ้า Method ไม่เหมือนกัน การทำงานจะต่างกัน เช่น

`localhost:8000/customer/1`

* หากเป็น GET Method อาจจะหมายถึงการดึงข้อมูล Customer ID 1
* หากเป็น PUT Method อาจจะหมายถึงการอัพเดทข้อมูล Customer ID 1
* หากเป็น DELETE Method อาจจะหมายถึงการลบข้อมูล Customer ID 1

`localhost:8000/project`

* หากเป็น GET Method อาจจะหมายถึงการดึงข้อมูล Project ทั้งหมด
* หากเป็น POST Method อาจจะหมายถึงการสร้างข้อมูล Project ตัวใหม่

***

## Class-Based View

จากหัวข้อ `write view in your app` เราได้เขียน View กันไปแล้ว แต่แบบนั้นเราเขียนเป็น `Function-Based View` ซึ่งจะยากต่อการจัดการเกี่ยวกับ Method ซึ่งการเขียน Class-Based View จะสามารถจัดการ Method ได้ง่ายกว่า โดยจะมีรูปแบบการเขียนดังนี้

<pre class="language-python"><code class="lang-python">from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import *
import json

class Customer(View):
    # get all post
    def get(self, request):
        customers = Customer.objects.all().values()
        return HttpResponse(json.dumps(list(customers)), content_type="application/json")
        
    # create new post
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
<strong>        body = json.loads(body_unicode)
</strong><strong>        Customer.objects.create(
</strong><strong>            first_name = body['first_name']
</strong><strong>            last_name = body['last_name']
</strong><strong>            email = body['email']
</strong><strong>            address = body['address']
</strong><strong>        )
</strong></code></pre>

จะเห็นว่าสามารถจัดการ Method ได้โดยการใช้ชื่อ function เช่น `def get()` จะหมายถึง Method GET, `def post()` จะหมายถึง Method POST ซึ่งสามารถใช้วิธีนี้กับ PUT และ DELETE

โดยวิธีนำไปใช้ใน `urls.py` จะมีวิธีแตกต่างกับตอนทำ function-based view ด้วย โดยจะใช้แบบนี้

<pre class="language-python"><code class="lang-python">from django.urls import path
from . import views

urlpatterns = [
    path("customer/", views.<a data-footnote-ref href="#user-content-fn-1">Customer</a>.<a data-footnote-ref href="#user-content-fn-2">as_view()</a>, name="employee")
]
</code></pre>

โดยวิธีใช้คือ `views.ClassName.as_view()`&#x20;

***

## csrf\_token

**csrf\_token** คือ token ที่ใช้ใน Django เพื่อป้องกันการโจมตีประเภท Cross-Site Request Forgery (CSRF) ซึ่งเป็นการโจมตีที่ hacker พยายามจะทำให้ผู้ใช้ส่งคำสั่งไปยัง Server โดยไม่รู้ตัว

token จะถูกสร้างขึ้นและฝังไว้ในฟอร์ม HTML เมื่อส่งฟอร์มนั้นไปยัง Server ระบบจะตรวจสอบว่าคำขอที่ได้รับมี token ที่ตรงกันหรือไม่ หากไม่มีหรือตรงกันไม่มี ระบบจะปฏิเสธ request นั้นเพื่อความปลอดภัย

โดยเวลาที่เราต้องการส่ง request ไปเราต้องใช้ csrf\_token ด้วย เพื่อให้ไม่โดนปฏิเสธ request

<pre class="language-javascript" data-title="script.js"><code class="lang-javascript">// สร้าง function ที่รับ csrf_token
function deleteProject(pro_id, <a data-footnote-ref href="#user-content-fn-3">csrf_token</a>){

    fetch(`/project/${pro_id}`, {
      method: 'DELETE',
      headers: {
          'Content-Type': 'application/json',
          // เมื่อเวลาที่ต้องการจะส่ง request ให้ส่ง csrf_token ไปด้วย
          <a data-footnote-ref href="#user-content-fn-4">'X-CSRFToken': csrf_token</a>
      },
  })
  .then(response => response.json())
  .then(data => {
      console.log('Item deleted successfully')
      window.location.reload()
  })
  .catch(error => console.error('Error:', error));
}
</code></pre>

<pre class="language-html"><code class="lang-html">{% load static %}

&#x3C;!DOCTYPE html>
&#x3C;html lang="en">
&#x3C;head>
    &#x3C;meta charset="UTF-8">
    &#x3C;meta name="viewport" content="width=device-width, initial-scale=1.0">
    &#x3C;link rel="stylesheet" href="{% static 'style.css' %}">
    &#x3C;title>{% block title %}{% endblock %}&#x3C;/title>
&#x3C;/head>
&#x3C;body>
    &#x3C;button onclick="deleteProject(1, <a data-footnote-ref href="#user-content-fn-5">{{ csrf_token }}</a>)">date project&#x3C;/button>
&#x3C;/body>
&#x3C;/html>
</code></pre>

{% hint style="danger" %}
csrf\_token ที่แนบไปต้องมาจาก csrf\_token ที่อยู่ใน template เท่านั้น gen เองก็แตกอยู่ดีนะครับ หรือก็คือ csrf\_token ต้องมาจาก `{{ csrf_token }}` เท่านั้น !!!
{% endhint %}

[^1]: ชื่อ Class ที่เขียน

[^2]: ใส่ `as_view()` ทุกครั้ง

[^3]: รับ csrf\_token

[^4]: ตอนที่ทำการส่ง request ให้ส่ง csrf\_token ไปด้วย

[^5]: ส่ง csrf\_token ไปที่ function
