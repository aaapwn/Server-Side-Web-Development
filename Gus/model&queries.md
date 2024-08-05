# Models & Queries

Source: https://djangocentral.com/django-orm-cheatsheet/

# Preface

Django, as a powerful and popular web framework, comes equipped with an impressive Object-Relational Mapping (ORM) system that simplifies database interactions and abstracts away much of the complexity involved in working with databases.

With its expressive and Pythonic syntax, developers can efficiently query, insert, update, and delete data from their database without writing raw SQL queries. Whether you are a beginner exploring the world of Django ORM or an experienced developer seeking a handy reference, this comprehensive cheatsheet will serve as your go-to guide for mastering the Django ORM.

# Model Definition

```python
from django.db import models

class MyModel(models.Model):
    field_name = models.CharField(max_length=100)
    another_field = models.IntegerField()
    date_field = models.DateTimeField(auto_now_add=True)
```

## Related Objects

```python
from myapp.models import MyModel, RelatedModel

# One-to-One Relationship
class MyModel(models.Model):
    related_model = models.OneToOneField(RelatedModel, on_delete=models.CASCADE)

# One-to-Many Relationship
class MyModel(models.Model):
    related_models = models.ForeignKey(RelatedModel, on_delete=models.CASCADE)

# Many-to-Many Relationship
class MyModel(models.Model):
    related_models = models.ManyToManyField(RelatedModel)
```

# Queryset Basics

```python
from myapp.models import MyModel

# Create objects
obj = MyModel.objects.create(field_name='value', another_field=42)

# Retrieve all objects
all_objects = MyModel.objects.all()

# Retrieve a single object
single_object = MyModel.objects.get(pk=1)

# Filter objects
filtered_objects = MyModel.objects.filter(field_name='value')

# Chaining filters
chained_filters = MyModel.objects.filter(field_name='value', another_field=42)

# Exclude objects
excluded_objects = MyModel.objects.exclude(field_name='value')

# Ordering
ordered_objects = MyModel.objects.order_by('field_name')

# Count objects
count_objects = MyModel.objects.count()

# Check if an object exists
exists = MyModel.objects.filter(field_name='value').exists()

# Delete objects
MyModel.objects.filter(field_name='value').delete()
```

## Related Objects Querying

```python
# Reverse relation
related_objects = RelatedModel.objects.filter(mymodel__field_name='value')

# Prefetch related objects (reduce queries)
my_objects = MyModel.objects.prefetch_related('related_models')
```

## Querying with Q Objects (Complex Queries)

```python
from django.db.models import Q

# OR query
q = Q(field_name='value') | Q(another_field=42)
or_query = MyModel.objects.filter(q)

# AND query
q = Q(field_name='value') & Q(another_field=42)
and_query = MyModel.objects.filter(q)
```

## Aggregation and Annotation

```python
from django.db.models import Avg, Sum, Count

# Aggregate functions
average_value = MyModel.objects.aggregate(avg=Avg('another_field'))
total_sum = MyModel.objects.aggregate(sum=Sum('another_field'))
total_count = MyModel.objects.aggregate(count=Count('pk'))

# Annotate (add calculated fields)
annotated_objects = MyModel.objects.annotate(avg=Avg('another_field'))
```

## F-Expression (Update and Annotate)

```python
from django.db.models import F

# Update fields with F-expression
MyModel.objects.update(another_field=F('another_field') + 10)

# Annotate with F-expression
annotated_objects = MyModel.objects.annotate(sum=F('another_field') + F('field_name'))
```

## Filtering with Lookups

```python
# Case-insensitive exact match
filtered_objects = MyModel.objects.filter(field_name__iexact='value')

# Contains
filtered_objects = MyModel.objects.filter(field_name__contains='value')

# Startswith and Endswith
filtered_objects = MyModel.objects.filter(field_name__startswith='prefix')
filtered_objects = MyModel.objects.filter(field_name__endswith='suffix')

# In
filtered_objects = MyModel.objects.filter(another_field__in=[1, 2, 3])

# Range
filtered_objects = MyModel.objects.filter(another_field__range=(10, 20))
```

## Date and Time Queries

```python
from datetime import date

# Exact Date Match
filtered_objects = MyModel.objects.filter(date_field__date=date(2023, 7, 31))

# Year, Month, Day
filtered_objects = MyModel.objects.filter(date_field__year=2023)
filtered_objects = MyModel.objects.filter(date_field__month=7)
filtered_objects = MyModel.objects.filter(date_field__day=31)

# Greater Than and Less Than
filtered_objects = MyModel.objects.filter(date_field__gt=date(2023, 7, 1))
filtered_objects = MyModel.objects.filter(date_field__lt=date(2023, 8, 1))
```

## Working with Aggregates and Grouping

```python
from django.db.models import Count, Sum

# Group by field_name and annotate
grouped_objects = MyModel.objects.values('field_name').annotate(count=Count('pk'))

# Group by field_name and calculate sum
grouped_objects = MyModel.objects.values('field_name').annotate(total_sum=Sum('another_field'))
```

## Hanlding Null and Empty Values

```python
# Filter for null values
filtered_objects = MyModel.objects.filter(field_name__isnull=True)

# Filter for empty strings (useful for CharField)
filtered_objects = MyModel.objects.filter(field_name='')

# Exclude empty strings
excluded_objects = MyModel.objects.exclude(field_name='')
```

## Chaining Querysets

```python
# Chain multiple filters
filtered_objects = MyModel.objects.filter(field_name='value').filter(another_field=42)

# Chain multiple excludes
excluded_objects = MyModel.objects.exclude(field_name='value').exclude(another_field=42)
```

## **Limiting QuerySets**

ในกรณีที่เราต้อง SELECT และต้องการ LIMIT ผลลัพธ์เราสามารถทำได้คล้ายๆ กับการ slice list ของ Python

```python
>>> Entry.objects.all()[:5] # LIMIT 5
>>> Entry.objects.all()[5:10] # OFFSET 5 LIMIT 5
```

**NOTE:** การใช้ negative index (`Entry.objects.all()[-1]`) นั้นไม่ support

# **Creating and Updating Objects**

```python
# Create and Save
obj = MyModel(field_name='value', another_field=42)
obj.save()

# Bulk Create (improves performance)
MyModel.objects.bulk_create([
    MyModel(field_name='value1', another_field=42),
    MyModel(field_name='value2', another_field=43),
])

# Update
MyModel.objects.filter(field_name='old_value').update(field_name='new_value')
MyModel.save()
```

## Saving ForeignKey and ManyToMany fields

การ update foreign key ก็สามารถทำได้เหมือนกับการ update field ปกติ โดยใช้ `save()`

```python
>>> from blogs.models import Blog, Entry
>>> entry = Entry.objects.get(pk=1)
>>> cheese_blog = Blog.objects.get(name="Cheddar Talk")
>>> entry.blog = cheese_blog # Update FK blog ของ entry (ID = 1) ไปที่ cheese_blog (name = "Cheddar Talk")
>>> entry.save()
```

แต่การ update ManyToManyField จะทำงานแตกต่างไปนิดหน่อย เราจะต้องใช้ `add()` ดังตัวอย่าง

สมมติเราต้องการ add instance `joe` เป็นหนึ่งใน `authors` ของ instance `entry` (ID = 1)

```python
>>> from blogs.models import Author
>>> joe = Author.objects.create(name="Joe")
>>> entry.authors.add(joe)
```

เราสามารถ `add()` ที่ละหลายๆ instances เข้าไปก็ได้

```python
>>> john = Author.objects.create(name="John")
>>> paul = Author.objects.create(name="Paul")
>>> george = Author.objects.create(name="George")
>>> ringo = Author.objects.create(name="Ringo")
>>> entry.authors.add(john, paul, george, ringo)
```

# **Defer and Only**

In Django's ORM, the **`defer()`** and **`only()`** methods are used to control which fields of a model are fetched from the database when querying. This can help improve performance by fetching only the necessary data and deferring the loading of less critical or heavier fields until they are actually accessed.

Here are practical examples of how to use **`defer()`** and **`only()`** in Django ORM queries:

Using **`only()`** to fetch only specific fields

```python
# Fetch only the publication years and ratings of books, loading all other fields
books = Book.objects.only('publication_year', 'rating')

for book in books:
    print(book.title, book.author)  # All fields except publication_year and rating are deferred
    print(book.publication_year, book.rating)  # These fields are loaded from the database
```

Using **`defer()`** to defer loading of specific fields

```python
# Fetch only the titles and authors of books, deferring other fields
books = Book.objects.defer('publication_year', 'summary', 'cover_image', 'rating', 'genre')

for book in books:
    print(book.title, book.author)  # Only these fields are loaded from the database
    # Accessing other fields will trigger database queries to load them
    print(book.publication_year, book.summary)
```

# Bulk Update with Values

```python
# Bulk update specific fields with given values
MyModel.objects.filter(field_name='old_value').update(field_name='new_value')
```

# Bulk Delete with Querysets

```python
# Bulk delete with a queryset
MyModel.objects.filter(field_name='value').delete()
```

# Aggregation Functions

```python
from django.db.models import Sum, Avg, Max, Min, Count

# Get the sum of a specific field
total_sum = MyModel.objects.aggregate(total_sum=Sum('field_name'))

# Get the average value of a specific field
average_value = MyModel.objects.aggregate(average_value=Avg('field_name'))

# Get the maximum value of a specific field
max_value = MyModel.objects.aggregate(max_value=Max('field_name'))

# Get the minimum value of a specific field
min_value = MyModel.objects.aggregate(min_value=Min('field_name'))

# Get the count of objects in the queryset
object_count = MyModel.objects.aggregate(object_count=Count('pk'))
```

# Exists Method

```python
# Check if at least one object exists in the queryset
exists_result = MyModel.objects.filter(field_name='value').exists()
```

# Delete

การลบข้อมูลออกจาก database สามารถทำได้โดยใช้ method `delete()`

ลบทีละตัว

```python
>>> e.delete()
(1, {'blog.Entry': 1})
```

ลบทีละหลายตัว

```python
>>> Entry.objects.filter(pub_date__year=2005).delete()
(5, {'blog.Entry': 5})
```

# Example
```python
>>> from company.models
>>> Company.objects.create(name="Company AAA", num_employees=120, num_chairs=150, num_tables=60)
>>> Company.objects.create(name="Company BBB", num_employees=50, num_chairs=30, num_tables=20)
>>> Company.objects.create(name="Company CCC", num_employees=100, num_chairs=40, num_tables=40)
```

```python
>>> from company.models import Company
>>> from django.db.models import Count, F, Value
>>> from django.db.models.functions import Length, Upper
>>> from django.db.models.lookups import GreaterThan

# Find companies that have more employees than chairs.
>>> Company.objects.filter(num_employees__gt=F("num_chairs"))

# Find companies that have at least twice as many employees as chairs.
>>> Company.objects.filter(num_employees__gt=F("num_chairs") * 2)

# Find companies that have more employees than the number of chairs and tables combined.
>>> Company.objects.filter(num_employees__gt=F("num_chairs") + F("num_tables"))

# How many chairs are needed for each company to seat all employees?
>>> company = (
...     Company.objects.filter(num_employees__gt=F("num_chairs"))
...     .annotate(chairs_needed=F("num_employees") - F("num_chairs"))
...     .first()
... )
>>> company.num_employees
50
>>> company.num_chairs
30
>>> company.chairs_needed
20

# Create a new company using expressions.
>>> company = Company.objects.create(name="Google", ticker=Upper(Value("goog")))
# Be sure to refresh it if you need to access the field.
>>> company.refresh_from_db()
>>> company.ticker
'GOOG'

# Expressions can also be used in order_by(), either directly
>>> Company.objects.order_by(Length("name").asc())
>>> Company.objects.order_by(Length("name").desc())

# Lookup expressions can also be used directly in filters
>>> Company.objects.filter(GreaterThan(F("num_employees"), F("num_chairs")))
# or annotations.
>>> Company.objects.annotate(
...     need_chairs=GreaterThan(F("num_employees"), F("num_chairs")),
... )
```

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Publisher(models.Model):
    name = models.CharField(max_length=300)

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
```

```python
>>> from books.models import Book
# Total number of books.
>>> Book.objects.count()
59

# Total number of books with publisher=Penguin Books
>>> Book.objects.filter(publisher__name="Penguin Books").count()
20

# Average price across all books, provide default to be returned instead
# of None if no books exist.
>>> from django.db.models import Avg
>>> Book.objects.aggregate(Avg("price", default=0))
{'price__avg': Decimal('9.7018644067796610')}

# Max price across all books, provide default to be returned instead of
# None if no books exist.
>>> from django.db.models import Max
>>> Book.objects.aggregate(Max("price", default=0))
{'price__max': Decimal('14.99')}

# All the following queries involve traversing the Book<->Publisher
# foreign key relationship backwards.

# Each publisher, each with a count of books as a "num_books" attribute.
>>> from books.models import Publisher
>>> from django.db.models import Count
>>> pubs = Publisher.objects.annotate(num_books=Count("book"))
>>> pubs
<QuerySet [<Publisher: BaloneyPress>, <Publisher: SalamiPress>, ...]>
>>> pubs[0].num_books
20

# Each publisher, with a separate count of books with a rating above and below 4
>>> from django.db.models import Q
>>> above = Publisher.objects.annotate(above_4=Count("book", filter=Q(book__rating__gt=4)))
>>> below = Publisher.objects.annotate(below_4=Count("book", filter=Q(book__rating__lte=4)))
>>> above[0].above_4
16
>>> below[0].below_4
4

# The top 5 publishers, in order by number of books.
>>> pubs = Publisher.objects.annotate(num_books=Count("book")).order_by("-num_books")[:5]
>>> pubs[0].num_books
39
```
