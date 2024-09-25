
# Charity Project in Django

This project is a website for a charity where people can register, log in, and sign up to volunteer. We use a database (PostgreSQL) to store user details, and everything is built using Python’s Django framework. Let's break down each step in a way that anyone can understand!

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [1. Setting Up the Virtual Environment](#1-setting-up-the-virtual-environment)
- [2. Installing Django](#2-installing-django)
- [3. Creating the Django Project](#3-creating-the-django-project)
- [4. Creating the App](#4-creating-the-app)
- [5. Setting Up URLs and Views](#5-setting-up-urls-and-views)
- [6. Organizing Templates and Static Files](#6-organizing-templates-and-static-files)
- [7. Updating Django Settings](#7-updating-django-settings)
- [8. Linking App URLs to Main Project](#8-linking-app-urls-to-main-project)
- [9. User Registration and Login](#9-user-registration-and-login)
- [10. Database Setup](#10-database-setup)
- [11. Creating Superuser and Applying Migrations](#11-creating-superuser-and-applying-migrations)
- [12. Handling Images and Files with Pillow](#12-handling-images-and-files-with-pillow)
- [13. Final Step: Run the Server](#13-final-step-run-the-server)

---

## Overview

The **Charity Project** is a website where people can sign up to help a charity. They can also log in, sign up to volunteer, and manage their account. All their information is safely stored in a database.

---

## Prerequisites

Before starting, you need to make sure you have these things installed on your computer:

- **Python 3.x**: This is the programming language we use to build the website.
- **Django**: A tool that helps us build websites quickly and easily.
- **PostgreSQL**: A place to store all the user data (like a big filing cabinet).
- **psycopg2**: A tool that helps Django talk to the PostgreSQL database.
- **Pillow**: A tool that helps Django handle pictures.

---

## 1. Setting Up the Virtual Environment

### Why?
A virtual environment is like a special room where we can work on our project without messing up anything else on the computer.

### Commands:
1. To create the virtual environment:
    ```bash
    python -m venv myenv
    ```
2. To start using it:
    ```bash
    myenv\Scripts\activate  # For Windows
    source myenv/bin/activate  # For Mac/Linux
    ```

If you see an error that says you can’t run scripts on Windows, type this:
```bash
Set-ExecutionPolicy RemoteSigned -Scope Process
```

---

## 2. Installing Django

### Why?
Django is the tool that makes building websites easier. It gives us shortcuts so we don’t have to build everything from scratch.

### Command:
```bash
pip install django
```

---

## 3. Creating the Django Project

### Why?
The Django project is like the main folder where all the code for our website will live.

### Commands:
1. To create the project:
    ```bash
    django-admin startproject myproject
    cd myproject
    ```
2. To check if it’s working, run the server:
    ```bash
    python manage.py runserver
    ```
Now, open your browser and type `http://127.0.0.1:8000/`. You should see a welcome page from Django!

---

## 4. Creating the App

### Why?
In Django, every part of the website is called an "app." We create an app to handle the charity functions like signing up to volunteer.

### Command:
```bash
python manage.py startapp myapp
```

---

## 5. Setting Up URLs and Views

### Why?
The URLs are like street addresses, telling your website where to go. Views are like instructions telling the website what to show when someone goes to a URL.

### Step 1: Set up URLs in `myapp/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```
This code means when someone visits the homepage (`/`), Django will show them what’s in the `home` view.

### Step 2: Create a view in `myapp/views.py`
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```
This code tells Django to show the `home.html` file when someone visits the homepage.

---

## 6. Organizing Templates and Static Files

### Why?
Templates hold the HTML (webpage structure), and static files (like CSS or images) make your website look nice.

### Organize Your Files:
1. Create folders for templates and static files:
    ```bash
    myproject/
        myapp/
            templates/
            static/
    ```
2. Put your `home.html` file inside the `templates` folder and your CSS and images inside `static`.

---

## 7. Updating Django Settings

### Why?
We need to tell Django where to find the HTML files (templates) and CSS/JS files (static files) so it can display them correctly.

### Step 1: Tell Django where to find templates (in `settings.py`):
```python
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

### Step 2: Tell Django where to find static files (in `settings.py`):
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

---

## 8. Linking App URLs to Main Project

### Why?
We want to connect the URLs of our app (`myapp`) to the main project so that all pages will work.

### Add the app’s URLs to `myproject/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # This connects the app’s URLs
]
```

---

## 9. User Registration and Login

### Why?
People need to register and log in to access the volunteer features. We'll create an `accounts` app to handle that.

### Step 1: Create the `accounts` app:
```bash
python manage.py startapp accounts
```

### Step 2: Add URLs for user actions in `accounts/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('volunteer/', views.volunteer, name='volunteer'),
]
```

### Step 3: Write the views in `accounts/views.py`:
- **Register**: This lets users create an account.
    ```python
    def register(request):
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
            user.save()
            return redirect('/')
        else:
            return render(request, 'register.html')
    ```
- **Login**: This checks the user’s details and logs them in.
    ```python
    def login(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                return HttpResponse("Invalid login details")
        else:
            return render(request, 'login.html')
    ```
- **Logout**: This logs the user out.
    ```python
    def logout(request):
        auth.logout(request)
        return redirect('/')
    ```

---

## 10. Database Setup

### Why?
The database stores all the important information like user details and volunteer registrations.

### Step 1: Tell Django to use PostgreSQL (in `settings.py`):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'charity',
        'USER': 'postgres',
        'PASSWORD': 'YourPassword',
        'HOST': 'localhost',
    }
}
```

---

## 11. Creating Superuser and Applying Migrations

### Why?
A superuser can access the admin panel to manage users and content. Migrations apply any changes made to the database.

### Step 1: Create a superuser:
```bash
python manage.py createsuperuser
```

### Step 2: Apply the database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 12. Handling Images and Files with Pillow

### Why?
The Pillow library helps Django work with images, which might be useful if you want to upload pictures.

### Step 1: Install Pillow:
```bash
pip install pillow
```

### Step 2:

 Tell Django where to store uploaded images (in `settings.py`):
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

## 13. Final Step: Run the Server

Once everything is set up, you can start the website by running this command:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see your charity website live!
