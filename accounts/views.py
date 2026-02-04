from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def user_register(request):

    if request.method == "POST":

        data = request.POST

        errors = {}

        username = str(data.get("username")).strip()
        password = str(data.get("password"))
        confirm_password = str(data.get("confirm_password"))

        if not username:
            errors["username"] = "username required"

        elif User.objects.filter(username=username).exists():
            errors["username"] = "Username already exists"

        if password != confirm_password:
            errors["password"] = "Password do not match"

        if errors:
            print(errors)
            return render(request, "accounts/register.html", context={
                'errors':errors.values(),
            })

        else:

            User.objects.create_user(username=username, password=password)
            return redirect("login")
    
    return render(request, "accounts/register.html")


def user_login(request):
    return render(request, "accounts/login.html")