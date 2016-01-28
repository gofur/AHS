from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from setting_proyek.models import Proyek

def login_view(request):

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
                return HttpResponseRedirect("/")
            else:
                messages.error(request, "Your account is not active, please contact the site admin.")
        else:
            messages.error(request, "Your username and/or password were incorrect.")

    return render(request, "login.html")

def index(request):
    if request.user.is_authenticated():
        query_set = Proyek.objects.filter(pengguna_id=request.user.id)
        context = {
                "object_list": query_set,
            }
        return render(request,"index.html", context)
    else:
        return HttpResponseRedirect("/login/")

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")