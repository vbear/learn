from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import BookInfo
from django.template import RequestContext,loader
def index(request):
    booklist = BookInfo.objects.all()
    template = loader.get_template('booktest/index.html')
    context = RequestContext(request,{'booklist': booklist})
    return HttpResponse(template.render(context))

def detail(request,id):
    book = BookInfo.objects.get(pk=id)
    #template = loader.get_template('booktest/detail.html')
    #context = RequestContext(request,{'book':book})
    #return HttpResponse(template.render(context))
    #return HttpResponse("detail %s" % id)
    return render(request,'booktest/detail.html',{'book':book})