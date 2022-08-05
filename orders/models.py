from django.db import models
from product.models import Burgers
from account.models import User


class Orders(models.Model):
    current_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=0)
    DELIVERY_TYPE = (
        ("Dostavka", "Доставка"),
        ("Samovizov", "Самовывоз")
    )
    PAYMENT_TYPE = (
        ("click", "Click"),
        ("payme", "Payme"),
        ("nalichniy", "Наличные")
    )
    delivery = models.CharField(max_length=20, choices=DELIVERY_TYPE)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE)
    address = models.CharField(max_length=300, null=True)
    kvartira = models.IntegerField(null=True, blank=True)
    podyezd = models.IntegerField(null=True, blank=True)
    etaj = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id} {self.user}"


class OrderDetail(models.Model):
    product = models.ForeignKey(Burgers, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    product_price = models.FloatField()
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    filial = models.ForeignKey("Filial", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.product} {self.number}"


class Filial(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"