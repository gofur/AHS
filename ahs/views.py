from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render


def login_user(request):

    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # message success
                messages.success(request, "You're successfully logged in!")
            else:
                messages.error(request, "Your account is not active, please contact the site admin.")
        else:
            messages.error(request, "Your username and/or password were incorrect.")

    return render(request, "login.html")

