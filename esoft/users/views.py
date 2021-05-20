from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserForm
from django.db.models.functions import Lower

from .models import User
import requests

def list_users(request):
    users = User.objects.all().order_by(Lower('name'), Lower('surname'))
    
    return render(request, 'users/list.html', {'users':users})

def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('/list/')
     
    response = requests.get('https://gerador-nomes.herokuapp.com/nome/aleatorio')
    
    data = response.json()
    surname = "%s %s" % (data[1],data[2])
    data_dict = {'name': data[0], 'surname': surname}

    form = UserForm(initial=data_dict)
    return render(request, 'users/new.html', {'form':form})

def view_user(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'users/view.html', {'user': user})

def update_user(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(instance=user)

    if(request.method == 'POST'):
        user = UserForm(request.POST, instance=user)

        if(user.is_valid()):
            user.save()
            return redirect('/list/')
        else:
            return render(request, 'users/update.html', {'form':form, 'user':user})
    else:
        return render(request, 'users/update.html', {'form':form, 'user':user})

def delete_user(request, id):
    user = get_object_or_404(User, pk=id)
 
    user.delete()

    return redirect('/list/')