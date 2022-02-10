from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'a.html', {'titles':'Django','link':'http://youtube.com'})
def profile(request):
    return render(request,'a.html', {'titles':'profile page','link':'http://127.0.0.1:8000/'})
def expression (request):
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a+2*b
    return render(request,'output.html',{'result':c})
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email_id']
        password=request.POST['password']

        x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        print("user created")
        return redirect('/')

    else:
        return render(request, 'b.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        from django.contrib import auth
        x=auth.authenticate(username=username,password=password)
        if x is not None:
            auth.login(request,x)
            return redirect('/')
        else:
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    print('helloworld')
    auth.logout(request)
    return redirect('/')
