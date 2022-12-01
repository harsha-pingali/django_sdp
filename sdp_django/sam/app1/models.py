from django.db import models


# Create your models here.
class User(models.Model):
    user_id=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    user_mail=models.EmailField(max_length=35)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    mobile=models.IntegerField()
