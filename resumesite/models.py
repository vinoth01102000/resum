from django.db import models

# Create your models here.

class Profile(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Mobile=models.IntegerField()
    Address=models.CharField(max_length=200)
    skill1=models.CharField(max_length=100)
    skill2=models.CharField(max_length=100)
    skill3=models.CharField(max_length=100)
    skill4=models.CharField(max_length=100)
    Experience1title=models.IntegerField()
    Experience1dur=models.IntegerField()
    Experiencedesc=models.IntegerField()
    Experience2title=models.IntegerField()
    Experience2dur=models.IntegerField()
    Experience2desc=models.IntegerField()
    Education1=models.CharField(max_length=100)
    Education1dur=models.CharField(max_length=100)
    Education1score=models.IntegerField()
    Education2=models.CharField(max_length=100)
    Education2dur=models.CharField(max_length=100)
    Education2score=models.IntegerField()
    #
    Education3 = models.CharField(max_length=100)
    Education3dur = models.CharField(max_length=100)
    Education3score = models.IntegerField()
    #


from django.contrib.auth.models import Group

class MyResume(models.Model):
    res=models.ForeignKey(Group,on_delete=models.CASCADE)
