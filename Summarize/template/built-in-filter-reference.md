# Built-in filter reference

**Built-in filters** ใน Django ช่วยในการจัดการกับข้อมูลที่จะแสดงในเทมเพลตโดยให้เราปรับแต่ง แปลง หรือจัดรูปแบบข้อมูลได้สะดวก โดยจะเปรียบเสมือนการใช้ฟังก์ชันหรือ method ใน python ปกติ เช่น

* การหาค่าความยาวของ string
  * django filter: `{{ value|length }}`
  * normal python: `length(value)`
* การตัดข้อความให้สั้นลง ("Hello World" -> "Hell...")
  * django filter: `{{ value|truncatechars:7 }}`
  * normal python: `value.truncatechars(7)`&#x20;

{% hint style="danger" %}
ไม่ใช่ว่าฟังก์ชันที่ python มีแล้วจะเอามาใช้แบบนี้ได้ ต้องใช้เฉพาะที่เขามีให้เท่านั้น อันนี้แค่เปรียบเทียบให้เห็นภาพเฉย ๆ น้า (ปกติ python มีฟังก์ชัน length มั้ยหล่ะ)
{% endhint %}

***

## add

เป็น filter ที่ใช้เพิ่มค่าจาก value เดิม โดยวิธีใช้คือ

```python
{{ value|add:2 }}
# หาก value มีค่าเป็น 2 ค่าที่แสดงออกไปจะเป็น 6
```

***

## cut

เป็น filter ที่ใช้ตัด string บางตัวออกจาก string ที่เราต้องการ เช่น

```python
# ตัด whitespace ออกจาก string
{{ value|cut:" " }}
# หาก value มีค่าเป็น "String with spaces" ค่าที่แสดงออกไปจะเป็น "Stringwithspaces"
```

***

## date, time

เป็น filter ที่ใช้จัด format ของเวลา โดยจะมี keyword ที่ใช้บ่อย ๆ ในการจัด format คือ

| Keyword | ความหมาย                           | ตัวอย่าง               |
| ------- | ---------------------------------- | ---------------------- |
| `D`     | ชื่อวันแบบย่อ                      | Sun, Mon, ...          |
| `l`     | ชื่อวันแบบเต็ม                     | Sunday, Monday, ...    |
| `d`     | วันที่                             | 01, 02, ..., 31        |
| `S`     | ตัวเรียงลำดับของตัวเลขในภาษาอังกฤษ | st, nd, rd, th         |
| `M`     | ชื่อเดือนแบบย่อ                    | Jan, Feb, ..., Dec     |
| `F`     | ชื่อเดือนแบบเต็ม                   | January, February, ... |
| `n`     | เดือนแบบเป็นตัวเลข                 | 01, 02, ..., 12        |
| `Y`     | ปี                                 | 2013, 2019 etc.        |
| `H`     | ชั่วโมงแบบ 24 ชม.                  | 00, 01, ..., 23        |
| `h`     | ชั่วโมงแบบ 12 ชม.                  | 01, 02, ..., 12        |
| `A`     | บอก AM, PM                         | AM, PM                 |
| `i`     | นาที                               | 00, 01, ..., 59        |
| `s`     | วินาที                             | 00, 01, ..., 59        |

```
{{ value|date:"D d M Y" }} {{ value|time:"H:i" }}
```

{% hint style="warning" %}
Keyword มันไม่เหมือน `strftime` นะ อย่างใช้สลับกัน&#x20;
{% endhint %}

***

## default, default\_if\_none

`default` คือการกำหนดค่าเริ่มต้นของตัวแปรต่าง ๆ หากตัวแปรนั้นนำไปแปลงเป็น booleam แล้วได้ `False` ก็จะแสดงค่า default ไปแทน

* ค่าที่แปลงเป็น boolean แล้วได้ `False` คือ `""` , `0` , `None` (`"False"` แปลงเป็น boolean ได้ True นะ ระวังไว้

```
{{ value|default:"nothing" }}
```

***

## dictsort

ใช่ในการเรียงค่าใน dictionary ว่าจะเรียงตาม key ตัวไหน เช่น

```html
{{ value|dictsort:"name" }}

<!-- ถ้าค่าของ value เป็น -->
[
    {"name": "zed", "age": 19},
    {"name": "amy", "age": 22},
    {"name": "joe", "age": 31},
]

<!-- จะได้ output -->
[
    {"name": "amy", "age": 22},
    {"name": "joe", "age": 31},
    {"name": "zed", "age": 19},
]
```

***

## join

ใช้ในการรวมสมาชิกของ iterable (เช่น list) เข้าด้วยกัน โดยแต่ละสมาชิกจะคั่นด้วย string ที่กำหนด เช่น

```python
{{ value|join:" // " }}

# หาก value มีค่าเป็น ['Apple', 'Banana', 'Cherry']
# output จะเป็น "Apple // Banana // Cherry"
```

***

## length

ใช้ในการหาความยาวของ string และ list โดยวิธีใช้คือ

```
{{ value|length }}
```

***

## truncatechars

ใช้ในการตัด string ให้สั้นลง โดยส่วนที่ตัดไปจะถูกแทนที่ด้วย `...`&#x20;

```python
{{ value|truncatechars:3 }}

# หาก value มีค่าเป็น "Hello" output จะออกเป็น "Hell..."
```

***

## filter from libraries

เราสามารถลง filter เพิ่มจาก library อื่น ๆ ได้ เช่น `humanize` โดยมีวิธีดังนี้

1. ลง library `pip install humanize`
2. เพิ่มใน INSTALLED\_APPS ใน settings.py `'django.contrib.humanize'`
3. นำไปใช้ได้เลย

<pre class="language-python"><code class="lang-python"><strong># load library มาใช้ คล้าย ๆ การ import
</strong><strong>{% load humanize %}
</strong>
# ใช้ได้เลย
{{ 45000|intcomma }}
# output จะเป็น 45,000 (ทำให้มนุษย์อ่านได้ง่ายขึ้น)
</code></pre>
