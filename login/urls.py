
from django.contrib import admin
from django.urls import path
from .views import login,signin,userentry

urlpatterns=[
    path('userlogin/',login,name="login"),
    path('usersignin/',signin,name="signin"),
    path('user_entry/',userentry,name="userentry"),
]

