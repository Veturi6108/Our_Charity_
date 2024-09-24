from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
# Create your views here.
def volunteer(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email)
        user.save()
        return redirect("#")
    else:
        return render(request, 'home.html') 