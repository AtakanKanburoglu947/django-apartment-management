from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from core.models import Profile,Content,Image,Comment,Message,Faq,Payment,Menu,Request,Setting
from django.http import HttpResponse
# Create your views here.

setting = Setting.objects.all().first
menus = Menu.objects.all()
@login_required(login_url='signin')
def index(request):
    contents = Content.objects.order_by('-created_at')
    first_content = Content.objects.latest('created_at')
    return render(request,'index.html',{'setting' :setting, 'contents': contents,'first_content':first_content,'menus':menus})

@login_required(login_url='signin')
def menu(request):

    return render(request,'menu.html',{'setting' :setting,'menus':menus})

@login_required(login_url='signin')

def contents(request,id):
    contents = Content.objects.filter(menu_id=id)
    menu_title = Menu.objects.get(id=id).title
    return render(request,'contents.html',{'contents':contents,'menu_title':menu_title,'menus':menus,'setting':setting})

@login_required(login_url='signin')

def gallery(request):
    images = Image.objects.all()
    return render(request,'gallery.html',{'images':images,'setting':setting,'menus':menus})

@login_required(login_url='signin')
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

    return render(request,'contact-us.html',{'setting':setting,'menus':menus})
@login_required(login_url='signin')
def request(request):
    user_profile = Profile.objects.get(user= request.user)
    user_id = user_profile.id_user
    if request.method == 'POST':
        subject = request.POST['subject']
        type = request.POST['type']
        message = request.POST['message']
        Request.objects.create(user_id=user_id,subject=subject,type=type,message=message,status=True)

    return render(request,'request.html',{'setting' :setting,'menus':menus})
def faq(request):
    faqs = Faq.objects.all()
    return render(request,'faq.html',{'faqs':faqs,'setting' :setting,'menus':menus})
@login_required(login_url='signin')
def payment(request):
    user_profile = Profile.objects.get(user= request.user)
    user_id = user_profile.id_user
    if request.method == 'POST':
        payment = request.POST['payment']
        Payment.objects.create(payment=payment,status=True,user_id=user_id)
        
    return render(request,'payment.html',{'setting' :setting,'menus':menus})
@login_required(login_url='signin')
def blog(request):
    contents = Content.objects.all().order_by('-created_at')
    return render(request,'blog.html',{'contents':contents,'setting' :setting,'menus':menus})
@login_required(login_url='signin')
def about(request):
    setting = Setting.objects.all().first
    return render(request,'about-us.html',{'setting':setting,'menus':menus})
@login_required(login_url='signin')  
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
    return render(request,'blog-item.html',{'content': content, 'comments':comments,'setting' :setting,'menus':menus})
@login_required(login_url='signin')  
def upload(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        description = request.POST['description']
        title = request.POST['title']
        keywords = request.POST['keywords']
        type = request.POST['type']
        new_image = Image.objects.create(image=image,title = title)
        menu_id = Menu.objects.get(title=type)
        new_image.save()
        new_content = Content.objects.create(id=new_image.content_id,
        image=image,description=description,
        keywords=keywords,
        title=title,
        type = type,
        menu_id = menu_id.id
        )
        new_content.save()
        return redirect('blog')
    contents = Content.objects.all()
    return render(request,'upload.html',{'contents': contents,'setting' :setting,'menus':menus})
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Hesap bulunamadı ')
            return redirect('signin')
    else:
        return render(request,'signin.html')
@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user= request.user)
    if request.method == 'POST':
        if request.FILES.get('image'):
            image = user_profile.image
            phone = request.POST['phone']
            address = request.POST['address']
            user_profile.image = image
            user_profile.phone = phone
            user_profile.address = address
            user_profile.save()
        else:
            image = request.FILES.get('image')
            phone = request.POST['phone']
            address = request.POST['address']
            user_profile.image = image
            user_profile.phone = phone
            user_profile.address = address
            user_profile.save()
        return redirect('/')
    return render(request,'settings.html',{'user_profile':user_profile,'menus':menus})

@login_required(login_url='signin')
def account(request=request):
    user_profile = Profile.objects.get(user= request.user)
    return render(request,'account.html',{'user_profile':user_profile,'setting' :setting,'menus':menus})

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')
def signup(request):  
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.info(request,'E-posta alınmış')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Kullanıcı adı alınmış')
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
        return render(request,'signup.html')
