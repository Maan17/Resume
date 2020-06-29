from django.db import models

# Create your models here.
class One(models.Model):
    about= models.TextField()
    head= models.CharField(max_length=25)
    backimg= models.ImageField(upload_to='backimg',null=True,blank=True)
    profimg= models.ImageField(upload_to='profimg',null=True,blank=True)