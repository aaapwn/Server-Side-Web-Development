# Layout

การทำ layout มีไว้เพื่อให้เราสามารถนำ layout ที่เราสร้างไว้ ไปใช้หน้าอื่น ๆ ได้โดยที่เราไม่ต้องเขียนโค้ดซ้ำซ้อน

{% code title="/myapp/template/layout.html" %}
```html
{% raw %}
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'style.css' %}">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block nav %}{% endblock %}

    <div class="head">
        {% block head %}{% endblock %}
    </div>

    {% block content %}
    {% endblock %}

    {% block script %}{% endblock %}
{% endraw %}
</body>
</html>
```
{% endcode %}

จะเห็นว่า เราสามารถเขียน Code เป็น layout เอาไว้ ซึ่งจะเห็น keyword `block` ซึ่งมันคือการกำหนด block เปรียบเสมือนว่า เรากำหนดช่องว่างไว้ตรงนี้ก่อน จะมีอะไรค่อยไปใส่ทีหลัง ซึ่งจะเห็นได้ว่ามีอยู่ 5 block โดยจะมี title, nav, head, content, script ซึ่ง เราสามารถนำมาใช้ได้โดย

```html
{% raw %}
{% extends 'layout.html' %}

{% block title %}this is title{% endblock %}

{% block head %}
<h1>Hello, World!</h1>
{% endblock %}

{% block content %}
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ullam, reiciendis.</p>
{% endblock %}
{% endraw %}
```

1. เริ่มจากการ `{% extends 'layout.html' %}` เพื่อที่เราจะดึง layout.html ที่ได้สร้างไว้มาใช้ <mark style="color:red;">**(ไว้ด้านบนสุดเท่านั้น!!!)**</mark>
2.  ต่อด้วยการที่ใส่สิ่งต่าง ๆ ไปไว้ใน block ต่าง ๆ ที่เราได้เตรียมไว้ โดยในกรณีนี้คือ

    &#x20;\- ใส่ `this is title` ใน block head

    &#x20;\- ใส่ `<h1>Hello, World!</h1>` ใน block head

    &#x20;\- ใส่ `<p>Lorem ipsum dolor sit ...</p>` ใน block content

    &#x20;\- ไม่จำเป็นต้องใช้ทุก block เช่นในตัวอย่างไม่ได้ใช้ nav และ script ซึงจะหมายความว่าเว้นว่างไป

โดยเมื่อเราใช้ได้ใช้ layout มาร่วมกันแล้ว สิ่งที่จะทำการ render ออกไปจะมีดังนี้

```haml
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% raw %}
{% static 'style.css' %}
{% endraw %}">
    <title>
    <!-- block title -->
    this is title
    <!-- endblock -->
    </title>
</head>
<body>
    <!-- block nav -->
    <!-- endblock -->

    <div class="head">
        <!-- block head -->
        <h1>Hello, World!</h1>
        <!-- endblock -->
    </div>

    <!-- block content -->
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ullam, reiciendis.</p>
    <!-- endblock -->
    
    <!-- block script -->
    <!-- endblock -->
</body>
</html>
```
