from django.shortcuts import render
from models import Customer, ProductCategory, Product, Cart, CartItem, Order, OrderItem, Payment, PaymentItem, PaymentMethod
from django.db.models import F
# Create your views here.

orders = Order.objects.filter(order_date__month=5)[:10]

for order in orders.values:
    print("%d %s")
