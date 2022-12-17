from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('settings/',views.settings,name='settings'),
    path('upload/',views.upload,name='upload'),
    path('blogs/<uuid:id>/',views.post,name='post'),
    path('blog/',views.blog,name='blog'),
    path('payment/',views.payment, name='payment'),
    path('faq/',views.faq, name='faq'),
    path('request/',views.request,name='request'),
    path('logout/',views.logout,name='logout'),
    path('account/',views.account,name='account'),
    path('about/',views.about,name='about'),
]