from django.db import models

class Contact(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=255, null=True)
    phoneNumber = models.CharField(max_length=9)
    mailAdress = models.CharField(max_length=100, default="")
    photoLink = models.CharField(max_length=155, null=True)

