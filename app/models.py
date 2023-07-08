from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cars(models.Model):

    cname = models.CharField(max_length = 150,primary_key = True)
    established = models.IntegerField()
    location = models.CharField(max_length = 150)
    cimage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    #branch = models.IntegerField()
    milage= models.CharField(max_length = 100)
    speed= models.IntegerField()
    description = models.TextField(default ='car')
    def __str__(self):
        return self.cname
        