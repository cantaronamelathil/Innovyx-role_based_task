

# Create your views here.
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserLoginForm
from django.contrib.auth.hashers import make_password



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = UserProfile.objects.get(username=username)
            print(user.password == make_password(password))
                
            if user is not None:
                login(request, user)
                if user.role == 'Admin':
                    return redirect('admin_dashboard')
                else:
                    return redirect('user_dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def admin_dashboard(request):
    if UserProfile.objects.get(username=request.user.username).role == 'Admin':
        users = UserProfile.objects.all().select_related()
        return render(request, 'admin_dashboard.html', {'users': users})
    return redirect('user_dashboard')

@login_required
def user_dashboard(request):
    if UserProfile.objects.get(username=request.user.username).role == 'User':
        return render(request, 'user_dashboard.html')
    return redirect('admin_dashboard')


def user_logout(request):
    logout(request)
    return redirect('login')
