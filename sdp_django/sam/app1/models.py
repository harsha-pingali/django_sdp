from django.db import models


# Create your models here.

class products(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="static/pics")
    cost=models.IntegerField()
    available=models.IntegerField()
    offer=models.BooleanField()
    discount=models.IntegerField()
    desc=models.TextField()
