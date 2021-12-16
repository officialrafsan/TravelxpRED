from django.db import models

# Create your models here.


class Post(models.Model):
    Post_title = models.CharField(max_length=100)
    Post_location = models.CharField(max_length=100)
    Post_tags = models.CharField(max_length=500)
    Post_description = models.TextField(max_length=1000000)