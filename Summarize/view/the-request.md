# The request

**HTTP Request** คือการร้องขอข้อมูลหรือบริการจากเซิร์ฟเวอร์ผ่าน Protocol HTTP ซึ่งเป็นการสื่อสารระหว่าง Client (เช่น Browser) กับ Server โดย Client จะส่ง Request ไปยัง Server เพื่อขอข้อมูล (เช่น หน้าสำหรับการแสดงผล) หรือสั่งให้ Server ทำงานบางอย่าง (เช่น การส่งข้อมูลไปบันทึกใน Database)

HTTP Request ประกอบด้วย:

* **Request Line:** บรรทัดแรกที่บอกว่าเราต้องการทำอะไร เช่นใช้ HTTP Method แบบ GET, POST, PUT, DELETE และระบุ Path ที่ต้องการ
* **Headers:** ข้อมูลเพิ่มเติมเกี่ยวกับคำขอ เช่น ประเภทของเบราว์เซอร์ ขนาดของข้อมูล การ Authentication หรือถ้าใน Django จะมี `csrf_token`
* **Body (Optional):** ข้อมูลที่ส่งไปกับคำขอ โดยเฉพาะอย่างยิ่งในคำขอประเภท POST หรือ PUT ที่มีข้อมูลเช่นแบบฟอร์มหรือไฟล์

***

## Handle HTTP Request in Django

บางครั้ง HTTP Request จะมีการส่งข้อมูลมาเพื่อประมวลผลที่ฝั่ง Server เช่น ส่งข้อมูล Customer คนใหม่มาเพื่อบันทึกข้อมูลลง Database โดยวิธีการส่งข้อมูลผ่าน HTTP Request ที่ได้ใช้บ่อย ๆ จะมีอยู่ด้วยกัน 2 รูปแบบหลัก ๆ คือ

* **URL Params** คือข้อมูลที่อยู่ใน URL เลย เช่น `localhost:8000/customer/1` โดยเลข 1 คือ id ของ Customer ที่จะส่งไปประมวลผลต่อที่หลังบ้าน
* **Body** คือข้อมูลที่ถูกส่งผ่านตัว request body โดยส่วนใหญ่แล้วจะใช้กับข้อมูลใน form เช่น `localhost:8000/register` จะเป็น url ที่ใช้สมัครสมาชิก โดยจะมีข้อมูลใน body

```json
{
    "first_name": "Satura",
    "last_name": "Torat",
    "email": "65070211@kmitl.ac.th",
    "address": {
        "planet": "world"
    }
}
```

***

## Handle URL Params

การจัดการข้อมูลที่ส่งผ่าน URL Params นั้นมีอยู่ 2 ขั้นตอนหลัก ๆ

1. สร้าง path ที่รองรับ URL Params

{% code title="urls.py" %}
```python
from django.urls import path
from . import views

urlpatterns = [
    path("project/<int:pk>", views.ManageProject.as_view(), name="project-edit"),
    path("staff/proj/<int:proj_id>/emp/<int:emp_id>", views.ManageStaff.as_view(), name="manage-staff"),
]
```
{% endcode %}

โดยจาก Code ตัวอย่างจะรับ 2 path คือ

* `/project/<int:pk>` โดย path นี้จะรับ params 1 ตัว คือ `pk` ที่มี datatype เป็น `int` ตัวอย่างเช่น `localhost:8000/project/3` ในที่นี้ `pk` จะมีค่าเท่ากับ 3
*   `staff/proj/<int:proj_id>/emp/<int:emp_id>` โดย path นี้จะรับ params 2 ตัว คือ

    * `proj_id` ที่มี datatype เป็น `int`&#x20;
    * `emp_id` ที่มี datatype เป็น `int`&#x20;

    ตัวอย่างเช่น `localhost:8000/staff/proj/2/emp/6` ในที่นี้ `proj_id` จะมีค่าเท่ากับ 2 และ `emp_id` จะมีค่าเท่ากับ 6

2. &#x20;สร้าง Views ที่รองรับ params

<pre class="language-python"><code class="lang-python"># project/&#x3C;int:pk>
class ProjectEditView(View):
    def get(self, request, <a data-footnote-ref href="#user-content-fn-1">pk</a>):
        project = Project.objects.get(pk=<a data-footnote-ref href="#user-content-fn-2">pk</a>)
        context = {
            "project": project,
            "start_date": project.start_date.strftime("%Y-%m-%d"),
            "due_date": project.due_date.strftime("%Y-%m-%d"),
        }
        return render(request, "project_detail.html", context)

    def delete(self, request, <a data-footnote-ref href="#user-content-fn-3">pk</a>):
        project = Project.objects.get(pk=<a data-footnote-ref href="#user-content-fn-4">pk</a>)
        project.delete()
        return JsonResponse({"status": "ok"})
</code></pre>

จะเห็นได้ว่าเราสามารถนำชื่อ params ที่ตั้งเอาไว้ตอนกำหนด path มาใส่ไว้ใน arguments ของ function views และสามารถนำตัวแปรนั้นไปใช้ได้เลย

***

## Handle Body

การดึงข้อมูลจาก Request body ตัวอย่างการใช้ดังนี้

```python
import json

class Register(View):
    def post(self, request):
        # ดึงข้อมูลจาก body
        body_unicode = request.body.decode('utf-8')
        # แปลงเป็น dict เพื่อเอาไปใช้งานต่อ
        body_data = json.loads(body_unicode)
        
        first_name = body['first_name']
        last_name = body['last_name']
        email = body['email']
        address  = body['address']
        
        Customer.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            address = address
        )
```

[^1]: เพิ่มชื่อ params ใน arguments ของ function

[^2]: นำ pk ที่รับมาไปใช้

[^3]: เพิ่มชื่อ params ใน arguments ของ function

[^4]: นำ pk ที่รับมาไปใช้
