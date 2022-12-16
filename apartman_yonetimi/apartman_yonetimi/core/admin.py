from django.contrib import admin
from .models import Profile,Content,Image,Faq,Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Content)
admin.site.register(Image)
admin.site.register(Faq)
admin.site.register(Comment)