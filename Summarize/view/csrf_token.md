# csrf\_token

**csrf\_token** คือ token ที่ใช้ใน Django เพื่อป้องกันการโจมตีประเภท Cross-Site Request Forgery (CSRF) ซึ่งเป็นการโจมตีที่ hacker พยายามจะทำให้ผู้ใช้ส่งคำสั่งไปยัง Server โดยไม่รู้ตัว

token จะถูกสร้างขึ้นและฝังไว้ในฟอร์ม HTML เมื่อส่งฟอร์มนั้นไปยัง Server ระบบจะตรวจสอบว่าคำขอที่ได้รับมี token ที่ตรงกันหรือไม่ หากไม่มีหรือตรงกันไม่มี ระบบจะปฏิเสธ request นั้นเพื่อความปลอดภัย

โดยเวลาที่เราต้องการส่ง request ไปเราต้องใช้ csrf\_token ด้วย เพื่อให้ไม่โดนปฏิเสธ request

<pre class="language-javascript" data-title="script.js"><code class="lang-javascript">// สร้าง function ที่รับ csrf_token
function deleteProject(pro_id, <a data-footnote-ref href="#user-content-fn-1">csrf_token</a>){

    fetch(`/project/${pro_id}`, {
      method: 'DELETE',
      headers: {
          'Content-Type': 'application/json',
          // เมื่อเวลาที่ต้องการจะส่ง request ให้ส่ง csrf_token ไปด้วย
          <a data-footnote-ref href="#user-content-fn-2">'X-CSRFToken': csrf_token</a>
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
    &#x3C;button onclick="deleteProject(1, <a data-footnote-ref href="#user-content-fn-3">{{ csrf_token }}</a>)">date project&#x3C;/button>
&#x3C;/body>
&#x3C;/html>
</code></pre>

{% hint style="danger" %}
csrf\_token ที่แนบไปต้องมาจาก csrf\_token ที่อยู่ใน template เท่านั้น gen เองก็แตกอยู่ดีนะครับ หรือก็คือ csrf\_token ต้องมาจาก `{{ csrf_token }}` เท่านั้น !!!
{% endhint %}

[^1]: รับ csrf\_token

[^2]: ตอนที่ทำการส่ง request ให้ส่ง csrf\_token ไปด้วย

[^3]: ส่ง csrf\_token ไปที่ function
