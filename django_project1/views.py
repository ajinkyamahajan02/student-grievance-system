from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import auth as a
from .models import GrievanceData

# Create your views here.
from django_project1.models import GrievanceData


def index(request):
    return render(request, 'index.html')


def teacher(request):
    return render(request, 'teacher_login.html')


def student_dash(request):
    if request.method == 'POST':
        query_email = request.POST['query_email']
        query_title = request.POST['query_title']
        obj = GrievanceData.objects.get(email=query_email, title=query_title)
        obj.stars = obj.stars+1
        obj.save()
        return HttpResponse("<script>alert('Liked! ');document.location='student_dash';</script>")
    else:
        allgrievances = GrievanceData.objects.all()
        return render(request, 'student_dash.html', {'allgrievances': allgrievances})


def teacher_dash(request):
    if request.method == 'POST':
        query_email = request.POST['query_email']
        query_title = request.POST['query_title']
        obj = GrievanceData.objects.get(email=query_email, title=query_title)
        obj.stars = obj.stars + 1
        obj.save()
        return HttpResponse("<script>alert('Liked! ');document.location='teacher_dash';</script>")
    else:
        allgrievances = GrievanceData.objects.all()
        return render(request, 'teacher_dash.html', {'allgrievances': allgrievances})


def username_exists(username):
    return User.objects.filter(username=username).exists()


def grievance(request):
    if request.method == 'POST':
        user = a.get_user(request)
        g_username = user.username
        print(g_username)
        g_email = user.email
        title = request.POST['title']
        desc = request.POST['desc']

        if title == "" or desc == "":
            return HttpResponse("<script>alert('Fill all details! ');document.location='grievance';</script>")
        else:
            query = GrievanceData.objects.create(username=g_username, email=g_email, title= title, desc=desc)
            query.save()
            return HttpResponse("<script>alert('Query sent! ');document.location='student_dash';</script>")
    else:
        return render(request, 'grievance.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        is_staff = request.POST['is_staff']

        if password1 == password2:
            if not username_exists(username):
                user = User.objects.create_user(username=username, email=email, password=password1)

                if is_staff == "teacher":
                    user.is_staff = True
                    user.save()
                    return HttpResponse(
                        "<script>alert('User created! ');document.location='teacher_login.html';</script>")
                if is_staff == "student":
                    user.save()
                    return HttpResponse("<script>alert('User created! ');document.location='index.html';</script>")
                return HttpResponse(
                    "<script>alert('Username already exists! '); document.location='index.html';</script>")
            else:
                return render(request, 'index.html')
        else:
            return HttpResponse("<script>alert('Passwords do not match. '); document.location='index.html';</script>")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        login_pass = request.POST['login_password']

        user = auth.authenticate(username=username, password=login_pass)

        if user is not None:
            auth.login(request, user)
            user = a.get_user(request)
            temp = user.is_staff

            if temp is True:
                return redirect("/teacher_dash")
            if temp is False:
                return redirect("/student_dash")
        else:
            return HttpResponse("<script>alert('Invalid credentials '); document.location='index.html';</script>")
    else:
        return render(request, 'index.html')
