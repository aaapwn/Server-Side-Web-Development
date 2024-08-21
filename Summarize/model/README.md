# Model

Software Requirements:

* [**PostgreSQL**](https://www.postgresql.org/download/) (Database)
* [**pgAdmin**](https://www.pgadmin.org/download/) (ตัวจัดการ Database)

***

## Django Models

เป็นส่วนประกอบใน Django ที่ใช้ในการสร้างและจัดการฐานข้อมูลโดยใช้โครงสร้างเชิง Object-Relational Mapping (ORM) ซึ่งช่วยให้เราทำงานกับฐานข้อมูลได้ง่ายขึ้นโดยไม่ต้องเขียน SQL โดยตรง โดยจะทำหน้าที่

1. **กำหนดโครงสร้างของข้อมูล:**
   * Django Models จะทำหน้าที่เป็นแม่แบบ (template) สำหรับข้อมูลที่เราจะเก็บในฐานข้อมูล โดยกำหนดฟิลด์ต่างๆ เช่น ชื่อ, อายุ, อีเมล ฯลฯ
2. **เชื่อมต่อกับฐานข้อมูลอัตโนมัติ:**
   * Django จะจัดการการเชื่อมต่อกับฐานข้อมูลให้โดยอัตโนมัติ เช่น การสร้างตาราง, การแก้ไขตาราง, และการลบข้อมูลตามโครงสร้างที่กำหนดใน Models
3. **สนับสนุน ORM:**
   * Django ORM ช่วยให้เราทำงานกับฐานข้อมูลผ่าน Python object เช่นการเพิ่มข้อมูล, อัพเดตข้อมูล, และดึงข้อมูลได้โดยไม่ต้องเขียน SQL

***

### Setting up

1. install `psycopg2` เพื่อการทำงานกับ PostgreSQL

{% code title="terminal" %}
```bash
pip install psycopg2
```
{% endcode %}

2. ทำการเชื่อมต่อ Database เข้ากับ Django

<pre class="language-python" data-title="/myproject/settings.py"><code class="lang-python"><strong>...
</strong><strong>
</strong><strong>DATABASES = {
</strong>    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "DATABASE_NAME",
        "USER": "DATABASE_USER",
        "PASSWORD": "DATABASE_PASSWORD",
        "HOST": "DATABASE_URL",
        "PORT": "DATABASE_PORT",
    }
}

...
</code></pre>

***

### Connect to pgAdmin

1. ใน pgAdmin คลิกขวาที่ Server Group (ในตัวอย่างคือ localhost) > Register > Server...

<figure><img src="../.gitbook/assets/image (3).png" alt="" width="334"><figcaption></figcaption></figure>

2. ใน tab General ใส่ชื่อตามที่ต้องการ

<figure><img src="../.gitbook/assets/image (4).png" alt="" width="375"><figcaption></figcaption></figure>

3. ใน tab Connection ใส่ Host Database

<figure><img src="../.gitbook/assets/image (5).png" alt="" width="375"><figcaption></figcaption></figure>

4. กด Save
