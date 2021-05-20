from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'users'

urlpatterns =  [
    path('', views.new_user, name='new_user'),    
    path('list/', views.list_users, name='list_users'),
    path('view/<int:id>/', views.view_user, name='view_user'),
    path('update/<int:id>/', views.update_user, name='update_user'),
    path('delete/<int:id>/', views.delete_user, name='delete_user'),
]