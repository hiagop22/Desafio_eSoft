from django.http.response import HttpResponse
from django.shortcuts import render

from .models import User

def new_user(request):
    return HttpResponse("hello")

def list_users(request):
    users = User.objects.all().order_by('name', 'surname')
    
    return render(request, 'users/list.html', {'users':users})


