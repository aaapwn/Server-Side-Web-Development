# Field Type

## Basic Field

<table><thead><tr><th width="155">Django Field</th><th width="193">Postgress Data Type</th><th>Description</th></tr></thead><tbody><tr><td>AutoField</td><td>-</td><td>Django จะเพิ่มคอลัมน์ <code>id</code> ที่เป็น PromaryKey &#x26; AutoIncrement ให้อัตโนมัติ </td></tr><tr><td>CharField</td><td><code>varchar</code></td><td>ข้อความสั้น ๆ ความยาวตามที่กำหนด</td></tr><tr><td>TextField</td><td><code>text</code></td><td>ข้อความยาว ๆ มีความยาวเท่าไหร่ก็ได้</td></tr><tr><td>EmailField</td><td><code>varchar</code></td><td>varchar ปกติที่ Django จะตรวจสอบ Email format ให้ </td></tr><tr><td>IntegerField</td><td><code>integer</code></td><td>จำนวนเต็ม</td></tr><tr><td>DecimalField</td><td><code>numeric</code></td><td>จำนวนทศนิยม</td></tr><tr><td>BooleanField</td><td><code>boolean</code></td><td>ค่าความจริง</td></tr><tr><td>DateField</td><td><code>date</code></td><td>วัน</td></tr><tr><td>TimeField</td><td><code>time</code></td><td>เวลา</td></tr><tr><td>DateTimeField</td><td><code>timestamp</code></td><td>วัน+เวลา</td></tr></tbody></table>

#### DecimalField

DecimalField จะใช้เก็บจำนวนทศนิยม โดยจะมี Attribute หลัก ๆ 2 ตัว ตือ

* `max_digits` ใช้กำหนดจำนวนหลักทั้งหมด ทั้งหน้าและหลังจุดทศนิยม
* `decimal_places` ใช้กำหนดจำนวนหลักทศนิยม

{% code title="Example" %}
```python
from django.db import models

class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
```
{% endcode %}

* **`price`**: กำหนดให้มี `max_digits=10` และ `decimal_places=2` ซึ่งหมายความว่าสามารถเก็บตัวเลขได้สูงสุด 10 หลัก โดยในนั้นมี 2 หลักหลังจุดทศนิยม เช่น `12345678.90`
* **`weight`**: กำหนดให้มี `max_digits=5` และ `decimal_places=2` ซึ่งหมายความว่าสามารถเก็บตัวเลขได้สูงสุด 5 หลัก โดยในนั้นมี 2 หลักหลังจุดทศนิยม เช่น `123.45`

***

## Relation Field

**Relation Type** มีด้วยกัน 3 ประเภท คือ

### One to One

ความสัมพันธ์ที่หนึ่งรายการเชื่อมโยงได้เพียงหนึ่งรายการของอีกตารางหนึ่ง เช่น 1 User มีได้เพียง 1 Profile และ 1 Profile มีได้เพียง 1 User ซึ่งใน Django จะใช้ `OneToOneField` ซึ่งจะใส่ฝั่งไหนก็ได้

<pre class="language-python"><code class="lang-python">from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = <a data-footnote-ref href="#user-content-fn-1">models.OneToOneField(User, on_delete=models.CASCADE)</a>
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
</code></pre>

### One to Many

ความสัมพันธ์ที่หนึ่งรายการเชื่อมโยงได้กับหลายรายการของอีกตารางหนึ่ง แต่หนึ่งรายการของอีกตารางหนึ่งจะเชื่อมโยงมาได้เพียงรายการเดียว เช่น 1 Author มีได้หลาย Blogs และ 1 Blog มีได้เพียง 1 Author โดยใน Django จะใช้ `ForeignKey` โดยจะต้องใส่ในฝั่ง **many** ซึ่งในที่นี้คือ Blog

<pre class="language-python"><code class="lang-python">from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = <a data-footnote-ref href="#user-content-fn-2">models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogs')</a>
</code></pre>

* `on_delete=models.CASCADE` เป็นการกำหนดว่า หาก Author ถูกลบ Blogs ทั้งหมดของ Author คนนั้นจะถูกลบด้วย
* `related_name='blogs'` คือการกำหนดชื่อ Relation&#x20;

### Many to Many

ความสัมพันธ์ที่หนึ่งรายการเชื่อมโยงได้กับหลายรายการของอีกตารางหนึ่ง และ หนึ่งรายการของอีกตารางหนึ่งสามารถเชื่อมโยงมาได้หลายรายการเช่นกัน เช่น Student 1 คนสามารถลงทะเบียนได้หลาย Subject และ 1 Subject ก็สามารถถูกลงทะเบียนโดยหลาย Student โดยใน Django จะใช้ `ManyToManyField` ซึ่งจะใส่ในฝั่งไหนก็ได้

<pre class="language-python"><code class="lang-python">from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=15, unique=True)
    subjects = <a data-footnote-ref href="#user-content-fn-3">models.ManyToManyField(Subject, related_name='students')</a>
</code></pre>



[^1]: this is one to one relation.

[^2]: this is one to many relation.

[^3]: this is many to many relation.
