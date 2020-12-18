from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPhoto(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo=models.ImageField(blank=True,null=True,upload_to="")
    def __str__(self):
        return self.user.username