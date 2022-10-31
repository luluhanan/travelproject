from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField()
    description=models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    cname=models.CharField(max_length=200)
    cimage=models.ImageField()
    qoutes=models.TextField()

    def __str__(self):
        return self.cname