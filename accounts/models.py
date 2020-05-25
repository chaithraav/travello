from django.db import models
from datetime import datetime
# Create your models here.

class review(models.Model):
    RATE_CHOICES = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    opinion = models.CharField(max_length = 1000)
    rate = models.CharField(max_length = 1, choices = RATE_CHOICES)