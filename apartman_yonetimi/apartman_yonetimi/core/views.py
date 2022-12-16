from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from core.models import Profile,Content
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='signin/')

def index(request):
    return render(request,'index.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('signin/')
    else:
        return render(request,'signin.html')
@login_required(login_url='signin/')
def settings(request):
    user_profile = Profile.objects.get(user= request.user)
    if request.method == 'POST':
        if request.FILES.get('image') == None:
            image = user_profile.image
            phone = request.POST['phone']
            address = request.POST['address']
            user_profile.image = image
            user_profile.phone = phone
            user_profile.address = address
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            phone = request.POST['phone']
            address = request.POST['address']
            user_profile.image = image
            user_profile.phone = phone
            user_profile.address = address
            user_profile.save()
        return redirect('settings')
    return render(request,'settings.html',{'user_profile':user_profile})
@login_required(login_url='signin/')  
def upload(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        description = request.POST['description']
        new_content = Content.objects.create(image=image,description=description)
        new_content.save()
    contents = Content.objects.all()
    return render(request,'upload.html',{'contents': contents})
def signup(request):  
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            else:
               user = User.objects.create_user(username=username,email=email,password=password)
               user.save()
               user_login = auth.authenticate(username=username,password=password)
               auth.login(request,user_login)
               user_model = User.objects.get(username=username)
               new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
               new_profile.save()
               return redirect('settings')
        else:
            messages.info(request,'Password does not match')
            return
    else:
        return render(request,'signup.html')
