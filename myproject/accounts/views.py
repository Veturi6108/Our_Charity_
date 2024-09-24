from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if(request.method == "POST"):
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            return HttpResponse("Enter Valid Details guru")
    else:
        return render(request,'login.html')
    
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email, password=password1,username=username)
        user.save()
        return redirect("/")
    else:
        return render(request, 'register.html') 
def volunteer(request):
        return render(request,'volunteer.html')
