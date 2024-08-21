# Querying

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

## Objects and QuerySet

#### Object

* Object คือ ชุดของข้อมูล 1 ชุดของข้อมูลใด ๆ เช่น ข้อมูลของ Customer  1 คน, ข้อมูลของ Product 1  ชิ้น เช่น

```python
# cus จะเป็น object
customer = Customer.objects.get(email = "65070185@kmitl.ac.th")
```

* โดย Object สามารถเข้าถึง attribure ต่าง ๆ ได้โดยการใช้จุด `.` ตามด้วยชื่อ attribute เช่น

```python
customer.first_name
# puwit

customer.last_name
# nunpan
```

#### QuerySet

* QuerySet คือ Set ของ ข้อมูลที่เราได้ทำการ Query มา โดยส่วนใหญ่จะเจอ 2 แบบ คือ
  * QuerySet Object คือ Set ของข้อมูลโดยที่ข้อมูลข้างในจะเก็บเป็น Object ซึ่งจะได้มาจากการทำ Query ปกติ
  * QuerySet Dictionary คือ Set ของข้อมูลโดยที่ข้อมูลข้างในจะเก็บเป็น Dictionary ซึ่งจะได้มากจากการใช้ method `values()` ของ QuerySet

<pre class="language-python"><code class="lang-python"><strong># customers_obj จะเป็น QuerySet Object
</strong><strong>customers_obj = Customer.objects.filter(email__endswith = "@kmitl.ac.th")
</strong># customers_obj จะเป็น QuerySet Dictionary
<strong>customers_dict = customers_obj.values()
</strong><strong>
</strong><strong># เข้าถึงโดยใช้ index ได้เหมือนกันทั้งคู่
</strong><strong>customers_obj[0]
</strong><strong>customers_dict[:10]
</strong><strong>customers_obj[5:10]
</strong><strong>
</strong># เข้าถึงโดยการใช้ for loop ของ QuerySet Object
<strong>for c in customers_obg:
</strong><strong>    print(c.first_name)
</strong><strong>    
</strong># เข้าถึงโดยการใช้ for loop ของ QuerySet Dictioonary
for c in customers_obg:
    print(c['first_name'])
</code></pre>

***

## Attribute

ในตารางต่าง ๆ ใน models จะมี attribute ของมัน ซึ่ง attribute ของแต่ละตารางจะมาจากชื่อ field ที่เรากำหนดใน `models.py` โดยแต่ละ attribute จะใช้แทนชื่อ Column ในตาราง เช่น

* Customer จะมี attribute: first\_name, last\_name, email, address
* Order จะมี attribute: customer, order\_date, remark

***

## all()

คือการ Query โดยการดึงข้อมูลทั้งหมดที่อยู่ในตารางนั้น ๆ ออกมาทั้งหมด โดยจะคืนค่าเป็น QuerySet หรือก็คือเป็น set ของ object เช่น

```python
# get all customer
> Customer.objects.all()
# <QuerySet [<Customer: Customer object (1)>, <Customer: Customer object (2)>, <Customer: Customer object (3)>, <Customer: Customer object (4)>, <Customer: Customer object (5)>, <Customer: Customer object (6)>]>

# get all product
> Product.objects.all()
# <QuerySet [<Product: Product object (1)>, <Product: Product object (2)>, <Product: Product object (3)>, <Product: Product object (4)>, <Product: Product object (5)>, <Product: Product object (6)>]>
```

***

## get() , filter()

`get()` และ `filter()` เปรียบเสมือน where condition ใน sql คือการ Query โดยมีเงื่อนไข โดยสามารถใส่ค่า attribute และกำหนดได้เลยว่าต้องการจะมีเงื่อนไขอะไรบ้าง ซึ่งความแตกต่างระหว่าง `get()` และ `filter()` คือ

* `get()` จะคืนค่าเป็น Object 1 ตัวเท่านั้น
  * หากไม่มีการคืนค่า หรือ หาข้อมูลไม่เจอตามที่เงื่อนไขได้กำหนด จะ Error ทันที
  * หากมีการคืนค่ามากกว่า 1 Object หรือ ข้อมูลที่หาเจอตามเงื่อนไขมีมากกว่า 1 ตัว จะ Error ทันที
* `filter()` จะคืนค่าเป็น QuerySet ไม่ว่าจะมีข้อมูล 1 ตัว, มากกว่า 1 ตัว หรือไม่มีก็ตาม

{% code title="get() example" %}
```python
# ดึงข้อมูลของ customer ที่มีชื่อเป็น Puwit และนามสกุลเป็น Nunpan
customer_get = Customer.objects.get(
    first_name = "Puwit",
    last_name = "Nunpan"
)
# เข้าถึงข้อมูล
customer_get.first_name
```
{% endcode %}

{% code title="filter() example" %}
```python
# ดึงข้อมูลของ customer ที่มีชื่อเป็น Puwit และนามสกุลเป็น Nunpan
customer_get = Customer.objects.filter(
    first_name = "Puwit",
    last_name = "Nunpan"
)
# เข้าถึงข้อมูล
customer_get[0].first_name
```
{% endcode %}

***

## Field Lookups

บางครั้งการ Query ข้อมูจำเป็นจะต้องมีการเขียน Query ซับซ้อนขึ้น เช่น สร้างขึ้นในเดือนพฤษภาคม, อีเมลลงท้ายด้วย "@kmitl.ac.th" เป็นต้น ซึ่งเราสามารถใช้ field lookups เพื่อเขียนเงื่อนไขที่ซับซ้อนเหล่านี้ได้โดย field loopups จะมี

<table><thead><tr><th width="158">Keyword</th><th>Description</th></tr></thead><tbody><tr><td>contains</td><td>ประกอบได้ด้วย</td></tr><tr><td>endswith</td><td>ขึ้นต้นด้วย</td></tr><tr><td>startswith</td><td>ลงท้ายด้วย</td></tr><tr><td>day</td><td>เช็ควัน (1-31)</td></tr><tr><td>month</td><td>เช็คเดือน (1-12)</td></tr><tr><td>year</td><td>เช็คปี</td></tr><tr><td>gt</td><td>มากกว่า</td></tr><tr><td>gte</td><td>มากกว่าหรือเท่ากับ</td></tr><tr><td>lt</td><td>น้อยกว่า</td></tr><tr><td>lte</td><td>น้อยกว่าหรือเท่ากับ</td></tr><tr><td>range</td><td>ระหว่าง (ใช้ได้กับ Integer หรือ Float เท่านั้น)</td></tr></tbody></table>

โดยวิธีใช้ keywords เหล่านี้เราสามารถใช้โดยการ `[attribute]__[keywords]` เช่น  ต้องการราคามากกว่า n คือ`price__gt`

```python
# หาข้อมูล Customer โดยต้องมี "wit" อยู่ในชื่อ
Customer.objects.filter(first_name__contains = "wit")

# หาข้อมูล Customer โดยอีเมลต้องเป็นของสถาบัน kmitl เท่านั้น
Customer.objects.filter(email__endswith = "@kmitl.ac.th")

# หาข้อมูล Customer โดยต้องเป็นนักศึกษา IT รหัส 65 เท่านั้น
Customer.objects.filter(email__startswith = "65070")

# หาข้อมูล Order โดยวันที่ทำการ Order ต้องเป็นวันที่ 16 เท่านั้น
Order.objects.filter(order_date__day = 16)

# หาข้อมูล Order โดยวันที่ทำการ Order ต้องเป็นเดือนพฤษภาคมเท่านั้น
Order.objects.filter(order_date__month = 5)

# หาข้อมูล Order โดยวันที่ทำการ Order ต้องเป็นปี 2024 เท่านั้น
Order.objects.filter(order_date__year = 2024)

# หาข้อมูล Payment โดยที่ราคาต้องมากกว่า 2000 บาท
Payment.objects.filter(price__gt = 2000)

# หาข้อมูล Payment โดยที่ราคาขั้นต่ำต้องอยู่ที่ 2500 บาท
Payment.objects.filter(price__gte = 2500)

# หาข้อมูล Payment โดยที่ราคาต้องน้อยกว่า 17500 บาท
Payment.objects.filter(price__lt = 17500)

# หาข้อมูล Payment โดยที่ราคามากที่สุดอยู่ที่ 15000 บาท
Payment.objects.filter(price__lte = 15000)

# หาข้อมูล Payment โดยที่ราคาต้องอยู่ในช่วง 5000 - 20000 บาท
Payment.objects.filter(price__range = (5000, 20000))

# หาข้อมูล Order โดยปีที่ทำการ Order ต้องอยู่ในระหว่างปี 2000 - 2024 เท่านั้น
Order.objects.filter(order_date__year__range = (2000, 2024))
# สามารถใช้ 2 Keyword ร่วมกันได้
```

***

## Work with relations

บางครั้ง model ของเราจะมีการทำ relation กับตารางอื่นด้วย ซึ่งเราสามารถใช้ Query ร่วมกับการทำ relation ได้โดยการเข้าถึง attribute ที่อยู่ใน model ได้เลย เช่น

* atrribute categories ของ model Product
* attribute customer ของ model Cart
* attribute order ของ Payment

และเมื่อเราเข้าถึง attribute relation ของ model ได้แล้ว เราก็จะสามารถเข้าถึง attribute ต่าง ๆ ที่อยู่ใน model ที่ทำการ relation ได้เลย ด้วยการใช้ `__` เช่น

```python
# หาข้อมูล Cart ที่มีเจ้าของชื่อ "puwit"
Cart.objects.filter(customer__name = "puwit")
# เข้าถึง attribute customer ของ Cart และเข้าถึง attribute name ของ Customer อีกที

# หาข้อมูล Product ที่อยู่ใน categories "Book"
Product.objects.filter(categories__name = "Book")
# เข้าถึง atrribute categories ของ Product และเข้าถึง attribute name ของ ProductCategory อีกที
```

จาก code models.py ด้านบน จะเห็นได้ว่า Product และ ProductCategory เชื่อมถึงกัน แต่จะเห็นได้ว่า มีเพียง Product เท่านั้นที่เข้าถึง ProductCategory ได้แต่ ProductCategory จะเข้าถึง Product ไม่ได้ เช่น

```python
# หาสิ้นค้าทั้งหมดที่อยู่ใน category book
ProductCategory.objects.get(name = "Book").product.all()
# error
```

เนื่องจากเดิม ProductCategory  ไม่มี attribute ที่ชื่อ product แต่ถ้าหากต้องการทำเช่นนี้เราสามารถใส่ related\_name ไว้ใน field ที่ทำ relation เพื่อที่จะให้สามารถเข้าถึงจากอีกฝั่งได้ เช่น เพิ่ม related\_name ใน field categories ของ Product เพื่อให้ ProductCategory สามารถเข้าถึง Product ได้ด้วย attribute "product"

<pre class="language-python"><code class="lang-python">class ProductCategory(models.Model):
    name = models.CharField(max_length=150)

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    remaining_amount = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(ProductCategory, <a data-footnote-ref href="#user-content-fn-1">related_name="product"</a>)
</code></pre>

แค่นี้เราก็จะสามารถเชื่อมต่อ relations ได้โดยสามารถเข้าถึงได้จากทั้ง 2 ฝั่ง

```python
# หาสิ้นค้าทั้งหมดที่อยู่ใน category book
ProductCategory.objects.get(name = "Book").product.all()
# no error
```

{% hint style="info" %}
ตอนทำแนะนำให้เปิดไฟล์ models.py ไปด้วย จะได้ดูได้ว่าแต่ละ model สามารถเข้าถึง attribute อะไรได้บ้าง เช่นดูว่า attribute customer ของ Cart สามารถเข้าถึง attribute อะไรได้อีกบ้าง
{% endhint %}

***

## Sort Data

เราสามารถ Sort ข้อมูลที่เราได้ทำการ Query มาได้ ซึ่งใน SQL เราจะใช้สิ่งที่เรียกว่า `ORDER BY` ส่วนใน Django เราก็จะใช้ `order_by()` และใส่ชื่อ field ที่ต้องการเรียงได้เลยเช่น

* `order_by('id')` เรียงตาม id **จากน้อยไปมาก**
* `order_by('-first_name')` เรียงตามชื่อ first\_name **จากมากไปน้อย**

จะเห็นได้ว่ามีการเรียง 2 แบบคือ มากไปน้อย และน้อยไปมาก โดย

* หากต้องการเรียงจากน้อยไปมาก ให้ใส่ชื่อ field นั้น ๆ ไปเลยตามปกติ
* หากต้องการเรียงจากมากไปน้อย ให้ใส่ชื่อ field โดยที่มี `-` นำหน้า

```python
# หาข้อมูล Product ที่มี category เป็น Information Technology โดยเรียงข้อมูลตาม `id` จากน้อยไปมาก
Product.objects.filter(
    categories__name="Information Technology"
).order_by("id")

# หาข้อมูล Customer ทั้งหมด โดยเรียงตามชื่อจาก Z-A
Customer.objects.all().order_by('-first_name')
```

***

## Q()

บางครั้งเราอาจจะต้องการ Query แบบมีเงื่อนไขนั้น ถ้าเขียน Query แบบเดิมถ้ามีมากกว่า 1 เงื่อนไขแล้ว การใช้ Comma `,` คั่นจะเหมือนการใช้ and condition แต่ถ้าหากต้องการจะใช้ or หรือ not condition แล้ว จะต้องใช้ `Q()` ร่วมด้วย โดยการใส่เงื่อนไขไว้ใน function `Q()` แล้วทำการเปรียบเทียบได้เลย โดย

* OR จะคั่นด้วย `|`
* NOT จะขึ้นต้นด้วย `~`

```python
from django.db.models import Q

# หาข้อมูล Customer โดยที่ชื่อจะต้องขึ้นต้นด้วย "p" หรือ "t" และต้องไม่ลงท้ายด้วย "e"
Customer.objects.filter(
    Q(first__name__startswith = "p") | Q(first_name__startswith = "t"),
    ~Q(first_name__endswith = "e"
)
```

***

## F()

บางครั้งเราต้องการจะเปรียบเทียบกับค่าใน field อื่น ๆ เช่น email ขึ้นต้นด้วยชื่อ firstname (ชื่อ puwit และอีเมลเป็น puwit@gmail.com) ซึ่งถ้าต้องการเปรียบเทียบแบบนี้เราจะต้องใช้ `F()` ช่วย ซึ่งสามารถใส่ชื่อ attribute ใน function `F()` และนำไปเปรียบเทียบได้เลย เช่น

```python
from django.db.models import F

# หาข้อมูล Customer โดยที่ email ต้องขึ้นต้นด้วยชื่อ firstname
# (เช่น ชื่อ puwit และอีเมลเป็น puwit123@gmail.com)

Customer.objects.filter(email__startswith = name)
# Error

Customer.objects.filter(email__startswith = F('name'))
# No error
```

{% hint style="info" %}
หากต้องการใส่ค่าที่มาจาก field อื่น ๆ ตอนทำ Query ต้องใส่ชื่อ field ใน function `F()` เท่านั้น
{% endhint %}

***

## annotate()

บางครั้งเราอยากได้ค่าอื่น ๆ มาแสดงผลด้วย เช่น ราคาสินค้าที่ลดราคาแล้ว, ชื่อเต็ม(ชื่อจริง, นามสกุล) ซึ่งเราสามารถสร้าง field แยกมาเพื่อใช้แสดงผล โดยที่ไม่กระทบต่อ database หลักได้ โดยสามารถกำหนดชื่อ field ใหม่และใส่ค่าไปได้เลย เช่น

<pre class="language-python"><code class="lang-python"># แสดงราคา Payment ที่ลาดราคาแล้ว โดยแสดงเฉพาะรายการแรก
# ไม่ใช้ annotate
Payment.objects.all()[0].after_discount
# error เนื่องจากไม่มี field นี้

Payment.objects.annotate(
    <a data-footnote-ref href="#user-content-fn-2">after_discount</a> = <a data-footnote-ref href="#user-content-fn-3">F('price') - F('discount')</a>
)[0].after_discount
# error เนื่องจากเราได้สร้าง field ชื่อ 'after_discount' ใน annotate แล้ว

# สามารถนำ function อื่น ๆ มาใช้ร่วมกันได้ เช่น
.filter().annotate().order_by()
.annotate().filter()
</code></pre>

โดยเราสามารถนำฟังก์ชันต่าง ๆ มาใช้ร่วมกับ `annotate()` ได้ โดยฟังก์ชันที่ใช้บ่อย ๆ คือ

* `Concat()` ใช้เพื่อต่อ String โดยจะใช้ร่วมกับ `Value()`&#x20;
* `Count()` นับว่ามีกี่แถวที่มีข้อมูลใน field นั้น โดยสามารถใช้ร่วมกับ `filter()` เพื่อทำให้นับแบบแยกหมวดหมู่ได้
* `Sum()` หาผลรวมของทุกค่าที่อยู่ใน field นั้น โดยสามารถใช้ร่วมกับ `filter()` เพื่อให้รวมแยกตาหมวดหมู่ได้

```python
# ชื่อ Customer เป็นชื่อเต็ม
Customer.objects.annotate(
    full_name = Concat(F('first_name'), Value(' '), F('last_name'))
)
# Concat ถ้าเป็นชื่อ field ให้ใส่ใน `F()` ถ้าเป็น string ธรรมดาให้ใส่ใน `Value()`

# นับจำนวนสินค้าที่อยู่ประเภท Electronics, Jewelry
ProductCategory.objects.filter(
    Q(name="Electronics") | Q(name="Jewelry"),
).annotate(
    product_count = Count('product__id')
)
# ใช้ `annotate()` ร่วมกับ `filter()`
```

***

## aggregate()

หากเราต้องการนำข้อมูลที่ได้มาคำนวนค่าต่าง ๆ เช่น ผลรวม, ค่าเฉลี่ย, ค่ามากสุด, ค่าน้อยสุด, นับจำนวน `aggregate()` สามารถนำมาใช้ได้ โดยใช้ร่วมกับฟังก์ชันต่าง ๆ โดยที่ใช้บ่อย ๆ จะมี

* `Sum('field_name')` หาผลรวมของทุกค่าที่อยู่ใน field นั้น
* `Avg('field_name')` หาค่าเฉลี่ยของทุกค่าที่อยู่ใน field นั้น
* `Count('field_name')` นับว่ามีกี่แถวที่มีข้อมูลใน field นั้น
* `Min('field_name')` ค่าที่น้อยที่สุดที่อยู่ใน field นั้น
* `Max('field_name')` ค่าที่มากที่สุดที่อยู่ใน field นั้น

กำหนดให้ข้อมูลของ Product มีดังนี้

<table><thead><tr><th width="68">id</th><th width="238">name</th><th width="212">description</th><th width="183">remaining_amount</th><th width="93">price</th><th>categories</th></tr></thead><tbody><tr><td>1</td><td>Iphone 99 pro evolution</td><td>Future iphone for you.</td><td>3</td><td>39990</td><td>1</td></tr><tr><td>2</td><td>Samsung Galaxy Milky way</td><td>Super samsung galaxy.</td><td>21</td><td>129990</td><td>2</td></tr><tr><td>3</td><td>Intel Core i79 99900KS</td><td>Best CPU in the world.</td><td>5</td><td>32990</td><td>3</td></tr></tbody></table>

{% code title="Example" %}
```python
from django.db.models import Sum, Avg, Count, Max, Min

# หาจำนวนสินค้าทั้งหมดที่เหลืออยู่
Product.objects.all().aggregate(sum = Sum('remaining_amount'))
# {'sum': 29} (3+21+5)

# หาค่าเฉลี่ยของราคาจากสินค้าทั้งหมด
Product.objects.all().aggregate(avg = Avg('price'))
# {'avg': Decimal('67656.666666666667')} ((39990+129990+32990)/3)

# นับจำนวนสินค้าว่ามีทั้งหมดกี่ชิ้น
Product.objects.all().aggregate(count_product = Count('id'))
# {'count_product': 3}

# หาว่าสินค้าชิ้นไหนราคาน้อยที่สุด
Product.objects.all().aggregate(min_price = Min('price'))
# {'min_price': Decimal('32990.00')}

# หาว่าสินค้าชิ้นไหนราคามากที่สุด
Product.objects.all().aggregate(max_price = Max('price'))
# {'max_price': Decimal('129990.00')}
```
{% endcode %}

{% hint style="danger" %}
`aggregate()` จะคำนวนจากข้อมูลทั้งหมดที่ Query ออกมาส่วน`.filter().annotate()` จะคำนวนข้อมูลโดยแยกตาม filter อย่าจำสับสนกันนะ ผลลัพธ์ไม่เหมือนกัน
{% endhint %}

<pre class="language-python"><code class="lang-python">ProductCategory.objects.filter(
    Q(name="Electronics") | Q(name="Jewelry"),
).<a data-footnote-ref href="#user-content-fn-4">annotate</a>(
    product_count = Count('product__id')
)
# &#x3C;QuerySet [{'id': 2, 'name': 'Electronics', 'product_count': 20}, {'id': 9, 'name': 'Jewelry', 'product_count': 5}]>

ProductCategory.objects.filter(
   Q(name="Electronics") | Q(name="Jewelry"),
).<a data-footnote-ref href="#user-content-fn-5">aggregate</a>(
    product_count = Count('product__id')
)
# {'product_count': 25}
</code></pre>

[^1]: เพิ่ม related\_name เพื่อให้ ProductCategory สามารถเข้าถึง Product ได้ด้วย attribute "product"

[^2]: ชื่อ field ใหม่

[^3]: ค่าของ field ใหม่

[^4]: ใช้ annotate

[^5]: ใช้ aggregate
