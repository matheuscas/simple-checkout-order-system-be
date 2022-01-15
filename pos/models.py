from django.db import models


class Category(models.Model):
    image_id = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)


class Order(models.Model):
    total = models.DecimalField(null=False, max_digits=11, decimal_places=2)


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    orders = models.ManyToManyField(Order, related_name='items')
    image_id = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(null=False, max_digits=11, decimal_places=2)
    quantity = models.IntegerField(null=False, default=1)



