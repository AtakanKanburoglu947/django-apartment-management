from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from core.models import Profile,Content,Image,Comment,Message,Faq,Payment,Menu,Request
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='signin/')
def index(request):
    return render(request,'index.html')

@login_required(login_url='signin/')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        Message.objects.create(name=name,email=email,phone=phone,
        subject=subject,message=message)
        return redirect('/contact')

    return render(request,'contact-us.html')
@login_required(login_url='signin/')
def request(request):
    user_profile = Profile.objects.get(user= request.user)
    user_id = user_profile.id_user
    if request.method == 'POST':
        subject = request.POST['subject']
        type = request.POST['type']
        message = request.POST['message']
        Request.objects.create(user_id=user_id,subject=subject,type=type,message=message,status=True)

    return render(request,'request.html')
def faq(request):
    faqs = Faq.objects.all()
    return render(request,'faq.html',{'faqs':faqs})
@login_required(login_url='signin/')
def payment(request):
    user_profile = Profile.objects.get(user= request.user)
    user_id = user_profile.id_user
    if request.method == 'POST':
        payment = request.POST['payment']
        Payment.objects.create(payment=payment,status=True,user_id=user_id)
        
    return render(request,'payment.html')
@login_required(login_url='signin/')
def blog(request):
    contents = Content.objects.all()
    return render(request,'blog.html',{'contents':contents})
@login_required(login_url='signin/')  
def post(request,id):   
    content = Content.objects.get(id=id)
    comments = Comment.objects.filter(content_id = id)
    user_profile = Profile.objects.get(user= request.user)
    content_id = content.id
    if request.method == 'POST':
        message = request.POST['comment']
        new_comment = Comment.objects.create(content_id=content_id,user_id = user_profile.id_user,comment=message)
        new_comment.save()
        return redirect('/blogs/'+str(content_id))
    return render(request,'blog-item.html',{'content': content, 'comments':comments})
@login_required(login_url='signin/')  
def upload(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        description = request.POST['description']
        title = request.POST['title']
        keywords = request.POST['keywords']
        new_image = Image.objects.create(image=image,title = title)
        new_image.save()
        new_content = Content.objects.create(id=new_image.content_id,image=image,description=description,keywords=keywords)
        new_content.save()
        return redirect('blog')
    contents = Content.objects.all()
    return render(request,'upload.html',{'contents': contents})
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
