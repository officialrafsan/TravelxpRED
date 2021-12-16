from django.db import models

# Create your models here.


class Admin(models.Model):
    Admin_name = models.CharField(max_length=100)
    Admin_email = models.CharField(unique=True, max_length=100)
    Admin_contact = models.IntegerField(unique=True)