from django.db import models

# Create your models here.
class One(models.Model):
    about= models.TextField()
    head= models.CharField(max_length=200)
    backimg= models.ImageField(upload_to='backimg',null=True,blank=True)
    profimg= models.ImageField(upload_to='profimg',null=True,blank=True)

class Career(models.Model):
    company=models.CharField(max_length=20)
    post=models.CharField(max_length=50)
    duration=models.CharField(max_length=50)
    job_desc=models.TextField()

class Two_main(models.Model):
    header=models.CharField(max_length=50)
    desc=models.TextField()

class Two_explaination(models.Model):
    features=models.CharField(max_length=20)
    features_desc=models.CharField(max_length=50)

class Projects(models.Model):
    image=models.ImageField(upload_to='projimg')
    feature=models.CharField(max_length=20)
    name=models.CharField(max_length=75)
    link=models.URLField()
    desc=models.TextField()