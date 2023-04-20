from django.db import models
from app.forms import *
# Create your models here.

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.sname
