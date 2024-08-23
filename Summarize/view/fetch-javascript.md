# Fetch JavaScript

`fetch` เป็นฟังก์ชันที่ใช้ใน JavaScript สำหรับการดึงข้อมูลจากเซิร์ฟเวอร์หรือ API แบบ HTTP request/response (ซึ่งเราอาจจะคุ้นเคยกับคำว่า "ยิง API" มากกว่า)

ซึ่งลักษณะการใช้จะเป็นการกำหนด URL endpoint หรือ API URL และก็กำหนดข้อมูลอื่น ซึ่งวิธีใช้จะเป็นแบบนี้

<pre class="language-javascript"><code class="lang-javascript">fetch('https://api.example.com/data/1',{ // กำหนด Endpoint URL
      method: 'POST', // กำหนด method
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': {{ csrf_token }} // กำหนด csrf_token
      },
      body: JSON.stringify(data) // กำหนด body หากมี
  })
  .then(response => response.json()) // แปลง response เป็น JSON
  .then(data => {
    console.log(data); // จัดการข้อมูลที่ได้จากการ fetch
  })
  .catch(error => {
<strong>    console.error('Error fetching data:', error); // ควรใส่ไว้เพื่อหา error ที่มันออกมา
</strong>  });
</code></pre>

โดยในตัวอย่างจะกำหนด

* URL Endpoint ซึ่งในที่นี้คือ `'https://api.example.com/data/1'`&#x20;
* กำหนด Method ซึ่งในที่นี้คือ `'POST'`&#x20;
* กำหนด Headers ซึ่งในที่นี้จะกำหนด
  * Content-type ซึ่งในที่นี้คือ  `'application/json'`&#x20;
  * X-CSRFToken ซึ่งหากต้องการยิง API ของ Django <mark style="color:red;">**เราต้องใส่ทุกครั้ง!!!**</mark>
* body (optional) ข้อมูลที่ต้องการจะส่งไปซึ่งส่วนใหญ่จะเป็น JSON (ที่แปลงเป็น String โดยการใช้ stringify)
