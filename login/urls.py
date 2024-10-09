
from django.contrib import admin
from django.urls import path
from .views import login,signin

urlpatterns=[
    path('userlogin/',login,name="login"),
    path('usersignin/',signin,name="signin"),
]

