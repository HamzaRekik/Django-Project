from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


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
        # Retrieve user data from POST request
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # Create new user
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        messages.success(request, "Your account has been created.")

    return render(request, "signin.html")


def contact(request):
    return render(request, "contact.html")


def logout_view(request):
    logout(request)
    return redirect("main")
