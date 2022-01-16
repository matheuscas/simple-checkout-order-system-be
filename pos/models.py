from django.db import models


class Category(models.Model):
    image_id = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)


class Payment(models.Model):
    class PaymentMode(models.IntegerChoices):
        CASH = 0
        CREDIT_CARD = 1
        DEBIT_CARD = 2

    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    address = models.TextField(max_length=200, null=False)
    payment_mode = models.IntegerField(choices=PaymentMode.choices, null=False)


class Order(models.Model):
    total = models.DecimalField(null=False, max_digits=11, decimal_places=2)
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)


class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )
    orders = models.ManyToManyField(Order, related_name="items")
    image_id = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(null=False, max_digits=11, decimal_places=2)
