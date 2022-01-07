from django.db import models

# Create your models here.


from UserManagement.models import User
from PostManagement.models import Post
class Comment(models.Model):
    Comment_description = models.CharField(max_length=5000)

    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.User.User_name