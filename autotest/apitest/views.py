from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from apitest.models import Apitest, Apistep


def test(request):
    return HttpResponse('hello world')


def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error'})
    return render(request, 'login.html')


def home(request):
    # return HttpResponse('hello world')
    return render(request, "home.html")


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


def apitest_manage(request):
    apitest_list = Apitest.objects.all()
    username = request.session.get('user', '')
    return render(request, "apitest_manage.html", {"user": username, "apitests": apitest_list})
