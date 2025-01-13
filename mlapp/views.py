from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Users

# Create your views here.

def userview(request):
    users=Users.objects.all().values()
    template=loader.get_template("user.html")
    context={
        'users':users
    }
    return HttpResponse(template.render(context,request))