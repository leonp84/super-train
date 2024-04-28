from django.db import models
from django.contrib.auth.models import User

PAYMENT = ((0, "Cash"), (1, "Credit"))


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.title


class Offer(models.Model):
    offer = models.FloatField()
    comment = models.TextField()
    payment = models.IntegerField(choices=PAYMENT, default=0)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product')
    created_on = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
