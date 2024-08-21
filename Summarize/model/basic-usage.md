# Basic Usage

**Models** คือการสร้างคลาสใน Python ที่ใช้แทนตารางในฐานข้อมูล โดยแต่ละคลาสจะมีการกำหนดฟิลด์ต่างๆ ซึ่งแทนคอลัมน์ในตาราง เช่นถ้าหากต้องการตารางที่มาลักษณะแบบนี้

<figure><img src="../.gitbook/assets/image (2).png" alt="" width="349"><figcaption></figcaption></figure>

จะสามารถเขียนใน Model ได้แบบนี้

{% code title="/myapp/models.py" %}
```python
from django.db import models

class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    posted = models.DateField()
    
```
{% endcode %}

เมื่อเขียนหรือแก้ไขในไฟล์ models.py เสร็จเรียบร้อยแล้ว สามารถนำไป Apply ใน Database ที่ได้ทำการ setting ไว้ ด้วยการทำ makemigrations และ migrate โดย

* makemigrations คือการสร้าง Statemenet เพื่อบอกว่ามีอะไรเปลี่ยนไปจากเดิมบ้าง เช่น เพิ่มตาราง  a, ลบคอลัมน์ b ในตาราง c ซึ่ง makemigrations จะทำการตรวจจับให้
* migrate คือการนำ Statement ที่ได้จากการทำ makemigrations ไป Apply ใน Database จริง ๆ

```bash
> python manage.py makemigrations
> python manage.py migrateba
```
