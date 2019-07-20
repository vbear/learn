from django.shortcuts import render
from apptest.models import Appcase, Appcasestep


# Create your views here.
def appcase_manage(request):
    appcase_list = Appcase.objects.all()
    username = request.session.get('user', '')
    return render(request, "appcase_manage.html", {"user": username, "appcases": appcase_list})
