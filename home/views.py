from django.shortcuts import redirect, render , get_object_or_404
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings



def home(request):
    content_1=Background.objects.first
    content_2=Category.objects.all()
    content_3=Product.objects.all()
    content_4=Partner.objects.all()
    content_5=News.objects.all()
    content_6=Founder.objects.all()



    context={
        "background_image":content_1,
        "categoryes":content_2,
        "products":content_3,
        "partners":content_4,
        "news":content_5,
        "founders":content_6,

    }
    return render(request,'index.html', context)

def news_details(request,pk):
    news= get_object_or_404(News,pk=pk)
    return render(request,'news_details.html',{'news':news})

def product_details(request,pk):
    products= get_object_or_404(Product,pk=pk)
    return render(request,'product_details.html',{'products':products})

def imprint(request):
    return render(request,'imprint.html')


def user_contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        CustomerMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            comment=message,
            gender=gender,
            lastname=lastname,
        )

        messages.success(request, "Your message has been sent.")
        return redirect('home')
    return render(request, 'contact.html')



def product(request):
    product=Product.objects.all()
    category=Category.objects.all()
    context={
        "products":product,
        "categoryes":category
    }
    return render(request,'product.html',context)

def team(request):
    founder=Founder.objects.all()
    context={
        "founders":founder
    }
    return render(request,'team.html',context)
#------------part of login View ---------------#

def login_user(request):
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user is not None:  # user is exsist in db
            login(request,user)
            messages.success(request, ("You Have been logged in."))
            return redirect('home')
        else:       #user is not in db
            messages.success(request, ("Oops! You are Not in System. "))
            return redirect('login')
    else:
        return render(request,'login.html')

#-------------part of logout View--------------#
def logout_user(request):
    logout(request)
    messages.success(request,("You Have been logged out !"))
    return redirect('home')

#-------------part of Reset Password View--------------#

def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            new_password = get_random_string(length=8)
            user.set_password(new_password)
            user.save()

            send_mail(
                subject='Password recovery',
                message=f'Your New password: {new_password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )

            messages.success(request, 'A new password has been sent to your email: {email}')
            return redirect('login')

        except User.DoesNotExist:
            messages.error(request, 'User with this email address not found!')

    return render(request, 'login.html')