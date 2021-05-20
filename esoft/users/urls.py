from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'users'

urlpatterns =  [
    path('', views.new_user, name='new_user'),    
    path('list/', views.list_users, name='list_users'),
]