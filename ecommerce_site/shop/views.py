from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Image
from .models import Pics  
from .models import Iphone
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import ContactMessage
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request, "home.html")

def products(request):
    return render(request, "products.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

from .models import Product

def cart(request):
    pics = Image.objects.all()
    return render(request, "cart.html", {"pics": pics})

def tv(request):
    pics = Pics.objects.all()   
    return render(request, 'tv.html', {'pics': pics})

def iphone_list(request):  
    pics = Iphone.objects.all()
    return render(request, "Iphone.html", {'pics': pics})


def homeimg1(request):
    return render(request, "homeimg1.html")

def homeimg2(request):
    return render(request, "homeimg2.html")

def homeimg3(request):
    return render(request, "homeimg3.html")

def home2(request):
     return render(request, "home2.html")
 
def ToolsThree(request):
     return render(request, "ToolsThree.html")
 
def ToolsTwo(request):
     return render(request, "ToolsTwo.html")
 
def Tools(request):
     return render(request, "Tools.html")
 
def footer(request):
     return render(request, "footer.html")
 
def product1(request):
     return render(request, "product1.html")
 
def product2(request):
     return render(request, "product2.html")
 
def product3(request):
     return render(request, "product3.html")
 
def product4(request):
     return render(request, "product4.html")
 
def product5(request):
     return render(request, "product5.html")
 
def product6(request):
     return render(request, "product6.html")
 
def product7(request):
     return render(request, "product7.html")
 
def product8(request):
     return render(request, "product8.html")
 
def product9(request):
     return render(request, "product9.html")
 
def product10(request):
     return render(request, "product10.html")
 
def product11(request):
     return render(request, "platform.html")


def navbar(request):
    return render (request, 'navbar.html')





# =========== login ==============

from django.contrib.auth import logout
from django.shortcuts import redirect

def LogoutPage(request):
    logout(request)
    return redirect('login')   

def SignupPage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        # ✅ check if username already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already taken")
            return redirect("signup")

        # ✅ check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("signup")

        # ✅ create user
        user = User.objects.create_user(username=uname, email=email, password=pass1)
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect("login")

    return render(request, "signup.html")

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')



from django.shortcuts import render
from .models import AboutVideo

def about(request):
    videos = AboutVideo.objects.all()[:6]  
    return render(request, "about.html", {"videos": videos})


# Create your views here.


def contact(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save to database
        ContactMessage.objects.create(name=name, email=email, message=message)
        
        # Send email
        send_mail(
            f"New Contact Message from {name}",
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        
        return JsonResponse({"success": True})
    
    return render(request, "contact.html")

