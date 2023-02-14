from shop .models import *
from django.db import models


class cart_list(models.Model):
    def __str__(self):
        return self.name

    cart_id = models.CharField(max_length=250, unique=True)
    date = models.DateField(auto_now_add=True)

class items(models.Model):
    def __str__(self):
        return self.prodt

    prodt = models.ForeignKey(product, on_delete=models.CASCADE)
    cart = models.ForeignKey(cart_list, on_delete=models.CASCADE)
    quty  =  models.IntegerField()
    active= models.BooleanField(default=True)


    def total (self):
        return self.prodt.price*self.quty





