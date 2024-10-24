from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    bio = models.TextField()
    image = models.ImageField(upload_to='photos/%Y%m%d')
    active = models.BooleanField(default=False)