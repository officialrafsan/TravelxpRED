from django.db import models

# Create your models here.


from UserManagement.models import User

class Post(models.Model):
    Post_title = models.CharField(max_length=100)
    Post_location = models.CharField(max_length=100)
    Post_tags = models.CharField(max_length=500)
    Post_description = models.TextField(max_length=1000000)

    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)