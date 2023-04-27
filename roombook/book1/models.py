from django.db import models
from django.core.validators import MinLengthValidator
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.
class Credentials(models.Model):
    Email=models.CharField(max_length=60,primary_key=True)
    Password=models.CharField(max_length=30)
    class Meta:
        db_table = 'User'

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=30)
    Sn_Sc=models.CharField(max_length=30)
    Email=models.ForeignKey(Credentials, on_delete=models.CASCADE, related_name='email', db_column='Email', blank=True)
    date = models.CharField(max_length=20,null=True, blank=True)
    room=models.CharField(max_length=20)
    time_slot = models.CharField(max_length=30,null=True, blank=True)
    reason = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'Book1'