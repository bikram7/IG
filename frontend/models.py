from django.db import models
from django.core.urlresolvers import reverse
class User(models.Model):
    name=models.CharField(50),
    username=models.CharField(30),
    password=models.CharField(30),
    course=models.CharField(30),
    year=models.IntegerField(30),
    branch=models.CharField(30),
    roll_no=models.IntegerField(30),
    reg_no=models.IntegerField(30),





