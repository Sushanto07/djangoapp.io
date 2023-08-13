# loginapp/views.py

from django.shortcuts import render
import os

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        with open(f'login_data_{username}.txt', 'w') as file:
            file.write(f'Username: {username}\nPassword: {password}')
        
    return render(request, 'login.html')
