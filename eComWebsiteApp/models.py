from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Userdata(models.Model):
    name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    subject= models.CharField(max_length=100,default="")
    message = models.CharField(max_length=300)
    
    def str(self):
        return self.name