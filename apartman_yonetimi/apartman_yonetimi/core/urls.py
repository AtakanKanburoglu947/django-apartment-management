from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact),
    path('signup',views.signup,name='signup'),
    path('signin/',views.signin),
    path('settings/',views.settings,name='settings')
]