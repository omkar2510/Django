
from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserForm
from .forms import UserForm
from django import forms
from django.contrib.auth.hashers import make_password
# Create your views here.


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request,'home.html',{'products':products,'categories':categories})

def about(request):
    return render(request,'about.html',{})

def login_users(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user )
            messages.success(request,("you have been login"))
            return redirect('home')
        else:
            messages.success(request,("There was an error, Please Try agin later........"))
            return redirect('login')
    else:

        return render(request,'login.html',{})

def logout_users(request):
    logout(request)
    messages.success(request,("You have been logout"))
    return redirect('home')

def register_users(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print("asdfasdfasdfasd")
            password1 = request.POST['password']
            password = make_password(password1)
            username = request.POST['username']
            obj = User(
                username=username,
                email=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                password=password
            )
            obj.save()
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user) 
                messages.success(request, "You have been logged in")
                return redirect('home')
            else:
                messages.error(request, "Authentication failed")
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password')
            if(username is not None):
                username = username
            else:
                username =request.POST['username']
            if(email is not None):
                email = email
            else:
                email =request.POST['email']
            if(first_name is not None):
                first_name = first_name
            else:
                first_name =request.POST['first_name']
            if(last_name is not None):
                last_name = last_name
            else:
                last_name =request.POST['last_name']
            if(password is not None):
                password = password
            else:
                password =request.POST['password']
            return render(request, 'register.html', {'form': form,'username':username,'email':email,'first_name':first_name,'last_name':last_name,'password':password})

    return render(request, 'register.html', {'form': UserForm()})


def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

def getcategory(request,id):

    categories = Category.objects.all()
    category = Category.objects.get(id=id)
    print("category==============",category)
    products = Product.objects.filter(category=category)
    # return render(request,'category.html')
    return render(request,'category.html',{'products': products,'category':category,'categories':categories})
    # except:
    # messages.success(request,("That Category Doesn't Exist........."))
    # return redirect('home')