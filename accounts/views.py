from django.shortcuts import render, redirect


# Create your views here.
def user_register(request):

    if request.method == "POST":

        data = request.POST

        errors = {}

        username = str(data.get("username"))
        password = str(data.get("password"))
        confirm_password = str(data.get("confirm_password"))

        if username is None and username == " ":
            errors["username"] = "username required"

        if password != confirm_password:
            errors["password"] = "Password do not match"
      
        if errors:
            redirect("register")

        else:
            redirect("login")
    
    return render(request, "accounts/register.html")