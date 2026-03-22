from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserCreationForm()
        
    return render(request, 'register.html', {'form': form})    

def home(request):
    return render(request, 'home.html')

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_only_view(request):
    return render(request, 'admin_page.html')