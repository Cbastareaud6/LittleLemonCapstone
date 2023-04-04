from django.db import models
from rest_framework import serializers
# Create your models here.

class Booking (models.Model):
    name = models.CharField(max_length=255)
    guestsnumber = models.IntegerField(6)
    bookingdate = models.DateTimeField(auto_now_add=True)


class Menu (models.Model):
    title=  models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(5)
    serializers.ModelSerializer



