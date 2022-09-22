from django.db import models
from account.models import User, Profile

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    quantity = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name



