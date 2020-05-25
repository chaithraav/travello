from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User,auth

# Create your models here.
class Places(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 200)
    price = models.IntegerField()
    image = models.ImageField(upload_to ='pics')
    offer = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class reservation(models.Model):
    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female','Female'),
    )
    name = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 10, choices = GENDER_CHOICES)
    age = models.IntegerField()
    no_of_people = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(10)])
    address = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    phone_no = models.CharField(max_length = 10, null=False, blank=False)
    place_id = models.ForeignKey(Places, null =True, on_delete =models.PROTECT)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default ='')
    

    def __str__(self):
        return self.name

class Payment(models.Model):
    CARD_CHOICES = (
        ('------','------'),
        ('debit','debit'),
        ('credit','credit'),
    )
    card = models.CharField(max_length = 20, choices = CARD_CHOICES,default=None, null=True, blank=False)
    card_no = models.CharField(max_length = 14, default=None, null=False, blank=False)
    cvv = models.CharField(max_length = 3, default=None, null=False, blank=False)
    expiry = models.CharField(max_length = 5, default=None, null=False, blank=False)
    email = models.EmailField(max_length = 254)
    
    
