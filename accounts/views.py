from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import RegisterForm

def home(request):
    return render(request, 'accounts/home.html')

def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )