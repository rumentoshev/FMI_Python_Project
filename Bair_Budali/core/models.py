from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# Every time you touch this file make migrations

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(
        upload_to='profile_images', default='10-Blank-Profile-Picture-with-Hat.png')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username