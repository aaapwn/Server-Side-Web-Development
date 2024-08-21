# Tag

ใน template เราสามารถใช้ tag ต่าง ๆ ได้ ซึ่ง tag ต่าง ๆ ก็เปรียบเสมือนคำสั่ง python ปกติ แต่ถ้าเราต้องการนำมารันใน template เราต้องนำมารันภายใต้ `{% tag %}`&#x20;

***

## autoescape

ใน html จะมีตัวอักษรบางตัวที่ไม่สามารถพิมพ์ได้โดยวิธีปกติอยู่ เช่น `<` หรือ `>` หากเราพิมพ์ไปในไฟล์ HTML มันจะเข้าใจว่ามัน คือ tag นึง แต่เราต้องการให้มันแสดงออกเป็น string เราเลยต้องใช้ escape character แทน เช่น

```html
<!-- ต้องการแสดง <script>alert("Hello")</script> ออกทางหน้าจอ -->

<!-- แบบนี้จะไม่ขึ้น เพราะจะเป็นการ run javascript แทน -->
<script>alert("Hello")</script>

<!-- เราเลยต้องทำแบบนี้ -->
&lt;script&gt;alert("Hello")&lt;/script&gt;
```

อ่านเพิ่ม: [https://mateam.net/html-escape-characters/](https://mateam.net/html-escape-characters/)

แต่ Django เราสามารถใช้ tag autoescape ได้เลย django จะทำการใช้ escape charactor เช่น

```html
{% raw %}
{% autoescape %}
<script>alert("Hello")</script>
{% endautoescape %}
{% endraw %}
```

{% hint style="danger" %}
ในทุก ๆ tag จะมีการ end เสมอ เช่น autoescape ก็จะมี endautoescape อย่าลืมใส่กันนะ
{% endhint %}

***

## block, extends

เป็น tag ที่ใช้สำหรับการทำ layout เรียนรู้เพิ่มเติมที่ [layout.md](layout.md "mention")

***

## for, empty

เหมือน for loop ใน python ปกติเลย แค่เอามาใช้ใน Django template แต่ใน django จะมี method ของ forloop ซึ่งสามารถใช้เป็นตัวแปรได้ เช่น

<table><thead><tr><th width="236">Variable</th><th>Description</th></tr></thead><tbody><tr><td><code>forloop.counter</code></td><td>จำนวน loop รอบปัจจุบัน (เริ่มจาก 1)</td></tr><tr><td><code>forloop.counter0</code></td><td>จำนวน loop รอบปัจจุบัน (เริ่มจาก 0)</td></tr><tr><td><code>forloop.first</code></td><td>ค่าจะเป็น True หากเป็นการ loop รอบแรก</td></tr><tr><td><code>forloop.last</code></td><td>ค่าจะเป็น True หากเป็นการ loop รอบสุดท้าย</td></tr></tbody></table>

อ่านเพิ่มเติม: [https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#for](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#for)

```html
<div class="itemGroup">
  {% raw %}
{% for project in projects %}
  <div class="item">
    <!-- โปรเจค id และ ชื่อ -->
    <div>{{forloop.counter}}. {{ project.name }}</div>

    <!-- วันเริ่ม และ วันกำหนดส่งโปรเจค -->
    <div>{{project.start_date}} - {{project.due_date}}</div>

    <div class="action">
      <!-- กำหนด path ให้ถูกต้อง -->
      <a href="{% url 'project-edit' project.id %}" class="edit btn">แก้ไข</a>

      <!-- ถ้า code มันแจ้งเตือนอะไรก็ปล่อยไปนะครับไม่มีผลอะไร  -->
      <button
        type="submit"
        onclick="deleteProject({{ project.id }}, '{{ csrf_token }}')"
        class="delete"
      >
        Delete
      </button>
    </div>
  </div>
  {% empty %}
  <div>no project found</div>
  {% endfor %}
{% endraw %}
</div>
```

จะเห็นได้มีการใช้ tag empty ร่วมด้วย ซึ่งจะทำงานร่วมกับ for loop โดยหาก for ไม่มีการ loop เกิดขึ้น จะทำงานที่ empty แทน โดยในตัวอย่างหมายถึง "`for` แสดงรายละเอียด project ทุกตัว หากไม่มี project หรือมัน `empty` จะแสดงว่า no project found"

***

## url

จะเห็น tag ที่ใช้อ้างอิงถึง path ที่เราได้สร้างไว้ โดยการอ้างอิงจะใช้ชื่อที่ได้ตั้งไว้ใน `urls.py` และสามารถระบุค่า url params ได้เลย เช่น

<pre class="language-python" data-title="urls.py"><code class="lang-python">from django.urls import path
from . import views

urlpatterns = [
    path("project/&#x3C;int:pk>", views.ProjectEditView.as_view(), name="<a data-footnote-ref href="#user-content-fn-1">project-edit</a>"),
    path("staff/proj/&#x3C;int:proj_id>/emp/&#x3C;int:emp_id>", views.ManageStaff.as_view(), name="<a data-footnote-ref href="#user-content-fn-2">manage-staff</a>"),
]
</code></pre>

<pre class="language-html" data-title=""><code class="lang-html">&#x3C;a href="{% url '<a data-footnote-ref href="#user-content-fn-3">project-edit</a>' <a data-footnote-ref href="#user-content-fn-4">project.id</a> %}" class="edit btn">แก้ไข&#x3C;/a>

&#x3C;a href="{% url 'manage-staff' project.id employee.id %}">ลบ Staff&#x3C;/a>
</code></pre>

[^1]: ชื่อของ path

[^2]: ชื่อของ path

[^3]: ชื่อของ path

[^4]: ค่าของ pk
