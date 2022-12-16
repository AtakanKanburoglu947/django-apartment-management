from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
import uuid
User = get_user_model()
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    phone = models.CharField(max_length=16,blank=True)
    image = models.ImageField(upload_to='profile_images',blank=True)
    address = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.user.username
class Content(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='content_images',blank=True)
    menu_id = models.IntegerField(blank=True,null=True)
    detail = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

