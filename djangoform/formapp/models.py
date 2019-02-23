from django.db import models


# Create your models here.
class Form(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    DEPARTMENT_CHOICES = (
        ('1', 'Dep1'),
        ('2', 'Dep2'),
        ('3', 'Dep3'),
    )
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.CharField(max_length=1, choices=DEPARTMENT_CHOICES)
    hiredDate = models.DateField()
    isPermanent = models.BooleanField()
