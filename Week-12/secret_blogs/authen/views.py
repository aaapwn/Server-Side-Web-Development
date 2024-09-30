from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User


class LoginView(View):
    
    def get(self, request):
        return render(request, 'login.html', {"form": None})
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog-list')
        else:
            messages.error(request, "Invalid username or password")

class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('login')
        
