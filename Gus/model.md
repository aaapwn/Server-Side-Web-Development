# Model

# Model fields ที่ใช้บ่อยๆ

[Doc](https://docs.djangoproject.com/en/5.0/ref/models/fields/)

# Fields types

- BooleanField(**options)

- CharField(max_length=None, **options)

- EmailField(max_length=254, **options)

- URLField(max_length=200, **options)

- UUIDField(**options)

- TextField(**options)

- DateField(auto_now=False, auto_now_add=False, **options)

- auto_now = True คือจะบันทึกค่า datetime.now() ทุกครั้งที่มีการแก้ไขค่า (INSERT + UPDATE)

- auto_now_add = True คือจะบันทึกค่า datetime.now() ตอนที่สร้างใหม่ (INSERT)

- DateTimeField(auto_now=False, auto_now_add=False, **options)

- TimeField(auto_now=False, auto_now_add=False, **options)

- FileField(upload_to='', storage=None, max_length=100, **options)

- upload_to คือกำหนด path ที่จะ save file

## Field Option

```python
- primary_key: ถ้ามีค่าเป็น True คือ column นี้เป็น primary key ของ table (ถ้าไม่กำหนด Django จะสร้าง column ชื่อ `id` ให้อัตโนมัติเป็น primary key)
- unique: ถ้ามีค่าเป็น True คือ ค่าใน column นี้ห้ามซ้ำ
- null: ถ้ามีค่าเป็น True คือ column นี้มีค่าเป็น null ได้
- blank: ถ้ามีค่าเป็น True คือ column นี้มีค่าเป็น "" หรือ empty string ได้
- default: กำหนดค่า default
- choices: กำหนด ENUM ให้เลือกเฉพาะค่าที่กำหนด
- db_index: ถ้ามีค่าเป็น True คือจะสร้าง index ใน database สำหรับ column นี้
```

**Example**
```python
class Student(models.Model):
    FRESHMAN = "FR"
    SOPHOMORE = "SO"
    JUNIOR = "JR"
    SENIOR = "SR"
    GRADUATE = "GR"
    YEAR_IN_SCHOOL_CHOICES = {
        FRESHMAN: "Freshman",
        SOPHOMORE: "Sophomore",
        JUNIOR: "Junior",
        SENIOR: "Senior",
        GRADUATE: "Graduate",
    }
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}
```
