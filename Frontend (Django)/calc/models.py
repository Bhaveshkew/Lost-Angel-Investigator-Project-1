from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key = True)
    image = models.ImageField(upload_to = 'images/')

class RegisteredChild(models.Model):
    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    age = models.IntegerField()
    mobile_num = models.CharField(max_length=15)
    image = models.ImageField(upload_to = 'registered_images/')

class User(models.Model):
    unique_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)


    