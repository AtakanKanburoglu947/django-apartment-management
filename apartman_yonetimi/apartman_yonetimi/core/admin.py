from django.contrib import admin
from .models import Profile,Content,Image,Faq,Comment,Menu,Message,Payment,Request

# Register your models here.
admin.site.register(Profile)
admin.site.register(Content)
admin.site.register(Image)
admin.site.register(Faq)
admin.site.register(Comment)
admin.site.register(Menu)
admin.site.register(Message)
admin.site.register(Payment)
admin.site.register(Request)