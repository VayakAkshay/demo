from django.db import models

# Create your models here.

class Generaldata(models.Model):
    name = models.CharField(max_length=50,default="")
    roll_no = models.IntegerField(max_length=231,default=0)
    desc = models.CharField(max_length=451,default="")
    
    def __str__(self):
        return self.name