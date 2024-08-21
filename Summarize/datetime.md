# Datetime

python มี module ชื่อ `datetime` อยู่ ซึ่ง module นี้มีไว้ใช้การทำงานต่าง ๆ เกี่ยวกับเวลา ซึ่งสามารถใช้ร่วมกับ Django ได้ เช่น เขียน Query&#x20;

* ที่เกี่ยวกับเวลา
* แสดงเวลาต่าง ๆ

***

## datetime

คือ function ที่ใช้แสดงวันและเวลา โดยจะมี class ที่ใช้บ่อย ๆ คือ

* `datetime(year, month, date, hours, mins, sec, milisec)`
* `date(year, month, date)`
* `time(hours, mins, sec, milisec)`

```python
from datetime import datetime, date, time

# get fix datetime
datetime(2024, 8, 20, 12, 0, 0, 0)
# get now datetime
datetime.now()

# get fix date
date(20, 8, 20)
# get now date
date.today()

# get time
time(12, 0, 0)
```

***

## Django Timezone

เวลาใน Django นั้นสามารถทำ timezone ได้โดยการไปกำหนดใน `settings.py` และกดหนดได้เลยว่าเป็น timezone ที่ไหน เช่นในตัวอย่างจะเป็น "Asia/Bangkok" โดยสามารถกำหนด timezone อื่น ๆ ได้ถ้าอยากรู้ว่ามี timezone อะไรบ้าง [https://pynative.com/list-all-timezones-in-python/](https://pynative.com/list-all-timezones-in-python/)

{% code title="/myproject/settings.py" %}
```python
...

# ปรับ timezone
TIME_ZONE = "Asia/Bangkok"

USE_I18N = True

#enable timezone
USE_TZ = True

...
```
{% endcode %}

โดยเราสามารถเรียกใช้เวลาตาม timezone ที่เรากำหนดใน settings.py ได้โดยการใช้ library timezone ของ django โดยจะมี 2  method หลัก ๆ คือ

* `timezone.now()` คืนค่าเป็นเวลาที่เป็น UTC
* `timezone.localtime()` คืนค่าเป็นเวลาตาม timezone ที่กำหนดใน settings.py

```python
from django.utils import timezone
from datetime import datetime

timezone.now()
# datetime.datetime(2024, 8, 20, 5, 18, 43, 660672, tzinfo=datetime.timezone.utc)

timezone.localtime()
# datetime.datetime(2024, 8, 20, 12, 18, 19, 396563, tzinfo=zoneinfo.ZoneInfo(key='Asia/Bangkok'))

datetime.now()
# datetime.datetime(2024, 8, 20, 12, 20, 4, 135415)
```

***

### Naive and Aware Datetime

จากหัวข้อ `Django timezone` จะเห็นได้ว่า datetime จะมีอยู่ 2 แบบ คือ

1. datetime ที่ไม่ได้บอก tzinfo หรือข้อมูล timezone เราจะเรียกประเภทนี้ว่า `Naive datetime`
2. datetime ที่บอก tzinfo หรือข้อมูล timezone เราจะเรียกประเภทนี้ว่า `Aware datetime`

ซึ่งเราสามารถใช้ function check ได้ คือ

```python
from django.utils import timezone
from datetime import datetime

t1 = timezone.now()
t2 = datetime.now()

# check is naive
timezone.is_naive(t1) # False
timezone.is_naive(t2) # True

# check is aware
timezone.is_aware(t1) # True
timezone.is_aware(t2) # False
```

โดยเราสามารถแปลงไปมาระหว่าว Naive และ Aware ได้โดยการใช้ function

* `timezone.make_naive()` แปลงเวลาให้เป็นประเภท naive
* `timezone.make_aware()` แปลงเวลาให้เป็นประเภท aware โดยจะยึด timezone ที่กำหนดใน settings.py

```python
timezone.make_naive(t1)

timezone.make_aware(t2)
```

***

## strftime()

`strftime()` เป็นฟังก์ชันที่เราสามารถแปลงเวลาให้เป็น format string ตามที่เราต้องการ โดยการเรียกใช้ Keyword ต่าง ๆ เช่น

```python
from datetime import datetime

datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
# '08/20/2024, 12:41:22'
```

โดย Keyword ต่าง ๆ ที่อาจจะใช้จะมี

| Keyword | ความหมาย           | ตัวอย่าง               |
| ------- | ------------------ | ---------------------- |
| `%a`    | ชื่อวันแบบย่อ      | Sun, Mon, ...          |
| `%A`    | ชื่อวันแบบเต็ม     | Sunday, Monday, ...    |
| `%d`    | วันที่             | 01, 02, ..., 31        |
| `%b`    | ชื่อเดือนแบบย่อ    | Jan, Feb, ..., Dec     |
| `%B`    | ชื่อเดือนแบบเต็ม   | January, February, ... |
| `%m`    | เดือนแบบเป็นตัวเลข | 01, 02, ..., 12        |
| `%Y`    | ปี                 | 2013, 2019 etc.        |
| `%H`    | ชั่วโมงแบบ 24 ชม.  | 00, 01, ..., 23        |
| `%I`    | ชั่วโมงแบบ 12 ชม.  | 01, 02, ..., 12        |
| `%p`    | บอก AM, PM         | AM, PM                 |
| `%M`    | นาที               | 00, 01, ..., 59        |
| `%S`    | วินาที             | 00, 01, ..., 59        |

Source: [https://www.programiz.com/python-programming/datetime/strftime](https://www.programiz.com/python-programming/datetime/strftime)
