from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View

def index(request):
    return render(request,'frontend/index.html')

