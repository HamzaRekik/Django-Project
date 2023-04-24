from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from portfolio.models import *
from services.models import *


def main(request):
    return render(request, "main.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")


def signin_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        messages.success(request, "Your account has been created.")

    return render(request, "signin.html")


def contact(request):
    # if User.is_authenticated():
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        contact = Contact.objects.create(name = name ,email= email , phone = phone , message = message)
    # else : 
    #     if request.method == "POST":
    #         text = request.POST.get("message")
    #         contact = Contact.objects.create(name = name ,email= email , phone = phone , text = text)
    return render(request, "contact.html")


def logout_view(request):
    logout(request)
    return redirect("main")


def blog_view(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "blog.html", context)

def article_view(request,pk):
    article = Article.objects.get(id=pk)
    return render(request, 'article.html',{'article':article})