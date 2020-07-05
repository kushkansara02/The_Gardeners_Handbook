from django.db import models
from django.contrib.auth.models import User


class Flower(models.Model):
    # default values
    name = models.CharField(max_length = 120, null = True, blank = True)
    lifecycle = models.CharField(max_length = 120, null = True, blank = True)
    sunRequirements = models.CharField(max_length = 120, null = True, blank = True)
    plantHeight = models.DecimalField(decimal_places=1, max_digits=3)
    structure = models.CharField(max_length = 120, null = True, blank = True)
    plantTime = models.CharField(max_length = 120, null = True, blank = True)
    flowerTime = models.CharField(max_length = 120, null = True, blank = True)
    waterCycle = models.DecimalField(decimal_places=0, max_digits=3, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    username = models.CharField(max_length = 120, null = True, blank = True)
    region = models.CharField(max_length = 120, null = True, blank = True)
    state = models.CharField(max_length = 120, null = True, blank = True)
    country = models.CharField(max_length = 120, null = True, blank = True)
    family_code = models.CharField(max_length = 120, null = True, blank = True)
    flowers = models.ManyToManyField(Flower)

    def __str__(self):
        return self.username


class WishList(models.Model):
    flowers = models.ManyToManyField(Flower, null=True, blank=True)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length = 120, null = True, blank = True)