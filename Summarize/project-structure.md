# Project Structure

## Project Structure

<figure><img src=".gitbook/assets/image (6).png" alt=""><figcaption><p>Django Structure</p></figcaption></figure>

<table><thead><tr><th width="140">File</th><th align="center">หน้าที่</th></tr></thead><tbody><tr><td>asgi.py</td><td align="center">ไฟล์สำหรับการตั้งค่า ASGI (Asynchronous Server Gateway Interface) เป็นเหมือน wsgi แต่สำหรับการจัดการโปรโตคอลที่ไม่ใช่ HTTP (เช่น WebSocket)</td></tr><tr><td>settings.py</td><td align="center">ไฟล์การตั้งค่าหลักของโปรเจค Django ซึ่งเก็บค่าคอนฟิกต่าง ๆ เช่น DATABASES, INSTALLED_APPS, TEMPLATES</td></tr><tr><td>urls.py</td><td align="center">ไฟล์ที่เก็บการตั้งค่า URL ของโปรเจค Django ใช้สำหรับกำหนด routing ของ URL ไปยัง views ต่าง ๆ</td></tr><tr><td>wsgi.py</td><td align="center">ไฟล์สำหรับการตั้งค่า WSGI (Web Server Gateway Interface) ซึ่งเป็นอินเตอร์เฟซมาตรฐานระหว่างเว็บเซิร์ฟเวอร์และโปรเจค Django ใช้ในการ deploy โปรเจค</td></tr><tr><td>manage.py</td><td align="center">Script สำหรับการจัดการและรันคำสั่งต่าง ๆ ในโปรเจค Django เช่น การ migrate database, การสร้างแอปใหม่, การรันเซิร์ฟเวอร์</td></tr></tbody></table>

***

## App Structure

<figure><img src=".gitbook/assets/image (7).png" alt=""><figcaption><p>App Structure</p></figcaption></figure>

<table><thead><tr><th width="154">File/Folder</th><th>หน้าที่</th></tr></thead><tbody><tr><td>migrations</td><td>โฟลเดอร์นี้เก็บไฟล์ migration ที่ใช้ในการติดตามการเปลี่ยนแปลงโครงสร้างของ Database</td></tr><tr><td>admin.py</td><td>ไฟล์สำหรับการตั้งค่า Admin Interface ของ Django ใช้ในการจัดการข้อมูลได้ผ่าน Admin Inteface</td></tr><tr><td>apps.py</td><td>ไฟล์สำหรับการตั้งค่าแอปพลิเคชัน ใช้ในการกำหนดค่าและการตั้งค่าต่าง ๆ ของแอปพลิเคชัน</td></tr><tr><td>models.py</td><td>ไฟล์ที่ใช้สำหรับการกำหนดโมเดล (Model) ของแอปพลิเคชัน ซึ่งโมเดลคือโครงสร้างของข้อมูลใน Database</td></tr><tr><td>tests.py</td><td>ไฟล์ที่ใช้สำหรับการเขียนเทสเคส (test cases) เพื่อทดสอบโค้ดและการทำงานต่าง ๆ ของแอปพลิเคชัน</td></tr><tr><td>views.py</td><td>ไฟล์ที่ใช้สำหรับการกำหนด view ของแอปพลิเคชัน ซึ่ง view คือส่วนที่จัดการกับการ request และ response ของเว็บแอปพลิเคชัน</td></tr></tbody></table>

***

## What is difference between "project" and "app"

**Project:**

* เป็นโครงสร้างหลักของ Web application ใน Django
* ประกอบด้วยการตั้งค่า, การกำหนดค่า URL, และการตั้งค่าทั่วไปอื่น ๆ
* สามารถมีได้หลาย app

**App:**

* เป็น Module สำหรับการเจาะจงการทำงาน เช่น Blogs, Todos
