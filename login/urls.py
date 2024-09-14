
from django.contrib import admin
from django.urls import path
from .views import login

urlpatterns=[
    path('userlogin/',login,name="login"),
]

