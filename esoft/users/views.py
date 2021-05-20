from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserForm
from django.db.models.functions import Lower

from .models import User

def list_users(request):
    users = User.objects.all().order_by(Lower('name'), Lower('surname'))
    
    return render(request, 'users/list.html', {'users':users})

def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('/list/')
     
    form = UserForm()
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