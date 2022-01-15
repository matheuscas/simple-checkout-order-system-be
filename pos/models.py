from django.db import models


class Category(models.Model):
    image_id = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)


class Order(models.Model):
    total = models.DecimalField(null=False, max_digits=11, decimal_places=2)


class Item(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', null=True)
    image_id = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(null=False, max_digits=11, decimal_places=2)



