# Add Update Delete

## Code Exmaplpe

กำหนดใน Code ใน `models.py`  มีดังนี้

```python
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    address = models.JSONField(null=True)

class ProductCategory(models.Model):
    name = models.CharField(max_length=150)

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    remaining_amount = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(ProductCategory)

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    expired_in = models.PositiveIntegerField(default=60)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    remark = models.TextField(null=True, blank=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    
class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.PROTECT)
    payment_date = models.DateField()
    remark = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class PaymentItem(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    order_item = models.OneToOneField(OrderItem, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
class PaymentMethod(models.Model):
    class MethodChoices(models.Choices):
        QR = "QR"
        CREDIT = "CREDIT"
    
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    method = models.CharField(max_length=15, choices=MethodChoices.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

***

## Add Data

เราสามารถสร้างข้อมูลโดยใช้คำสั่ง `Model.objects.create()` ได้เลย ตัวอย่างเช่น

<pre class="language-python"><code class="lang-python"><strong># เพิ่งข้อมูล Customer
</strong><strong>Customer.objects.create(
</strong>    first_name = "Puwit",
    last_name = "Nunpan",
    email = "65070185@kmitl.ac.th"
    address = {'planet':'world'}
)

# สร้าง Order โดยให้มีเจ้าของเป็น Customer ที่ชื่อ "Sila"
sila = Customer.objects.get(first_name = "Sila")
Order.objects.create(
    <a data-footnote-ref href="#user-content-fn-1">customer = sila</a>,
    create_date = date(2024, 8, 20),
    remark = "order by sila kak kak"
)
</code></pre>

จะเห็นได้ว่า สามารถสร้าง โดยกำหนดค่าตามปกติได้เลย แต่ถ้าหากเป็น field ที่เป็น relation สามารถกำหนดค่าเป็น Object ที่ต้องการได้ได้เลย เช่นตัวอย่างข้างต้น field customer เป็น relation ที่เชื่อมกับ Model Customer ดังนั้นแล้วเราสามารถนำ Object ที่เป็นของ Model Customer `(Sila)` มาใช้กำหนดค่าได้เลย

***

## Update Data

เราสามารถ Update ข้อมูลโดยการที่เรา Query ข้อมูล และแก้ attribute ได้เลย เช่น

```python
# เปลี่ยน email ของ "Puwit" ให้เป็น "it65070185@it.kmitl.ac.th"
puwit = Customer.objects.get(name = "Puwit")
puwit.email = "it65070185@it.kmitl.ac.th"
puwit.save()

# เปลี่ยนเจ้าของ Order ที่มี remark คือ "order by sila kak kak" เป็นของ Customer ชื่อ "Saruta"
order = Order.objects.get(remark = "order by sila kak kak")
bamboo = Customer.objects.get(first_name = "Saruta")
order.customer = bamboo
order.save()
```

{% hint style="warning" %}
หาก Update ด้วยวิธีแก้ attribute อย่าลืม `save()` ทุกครั้ง
{% endhint %}

***

## Many to Many field

หากต้องการสร้างหรือเปลี่ยนข้อมูล หากเป็น One to One หรือเป็น One to Many เราก็สามารถสร้างหรือแก้ไขด้วยวิธีปกติได้เลย แต่หากเป็น Many to Many ซึ่งสามารถเป็นได้หลายค่า ไม่ได้มีแค่ค่าเดียว เราต้องใช้ `add()` และ `remove()` ช่วยโดย

* `add()` ใช้เพื่อเพิ่มค่าใหม่เข้าไปใน relation
* `remove()` ใช้เพื่อลบค่าเก่าออกจาก relation

<pre class="language-python"><code class="lang-python"># สร้าง Product
robot = Product.object.create(
    name = "Robot",
    description = "This is robot for kids",
    remaining_amount = 20,
    price = 9990,
)
# ยังไม่ต้องใส่ categories

# get object ที่ต้องการ
<strong>toys = ProductCategory.objects.get(name = "Toys")
</strong>elec = ProductCategory.objects.get(name = "Electronics") 

# เพิ่มหมวดหมู่ Toys และ Electronics ให้กับ Product Robot
robot.categories.add(toys)
robot.categories.add(elec)
# categories คือชื่อ field relations ที่เราใส่ไปตอนสร้าง model

# ลบหมวดหมู่ Toys ออกจาก Product Robot
robot.categories.remove(toys)
</code></pre>

***

## Delete data

เราสามารถลบข้อมูลใด ๆ โดยการใช้ `delete()` ได้เลย เช่น

```python
# ลบ Sila ออกจากตาราง Customer
sila = Customer.objects.get(first_name = "Sila")
sila.delete()

# ลบ Robot ออกจากตาราง Product
robot = Product.objects.get(name = "Robot")
robot.delete()
```

[^1]: สามารถใช้ sila ที่ได้ทำการ Query มาได้เลย
