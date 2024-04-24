from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ...

class Stock(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, related_name='stocks', on_delete=models.CASCADE)
    username = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)

