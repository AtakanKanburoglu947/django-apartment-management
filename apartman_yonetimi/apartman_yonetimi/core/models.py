from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    phone = models.CharField(max_length=16,blank=True)
    image = models.ImageField(upload_to='profile_images',default='blank-profile-photo.jpg')
    address = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.user.username

