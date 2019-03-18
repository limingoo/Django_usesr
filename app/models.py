from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=17,unique=True)
    password=models.CharField(max_length=20)
    sex=models.CharField(max_length=2)
    age=models.IntegerField(default=1)
    class Meta():
        db_table="users"