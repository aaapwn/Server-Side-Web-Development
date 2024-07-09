from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    address = models.JSONField()

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    remaining_amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Cart(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField('date created')
    expried = models.IntegerField(default=60)

class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

class ProductCategory(models.Model):
    name = models.CharField(max_length=150)

class product_category(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_id = models.IntegerField(primary_key=True)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date ordered')
    remarks = models.TextField()

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

class Payment(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, unique=True)
    payment_date = models.DateTimeField('date paid')
    remarks = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)

class PaymentItem(models.Model):
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    order_item_id = models.ForeignKey(Order, on_delete=models.CASCADE, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class PaymentMethod(models.Model):
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    method = models.CharField(choices=[
        ("QR", "QR"),
        ("CREDIT", "CREDIT"),
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)
