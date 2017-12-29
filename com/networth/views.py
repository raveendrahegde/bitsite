from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from networth.forms import SignUpForm


def home(request):
    return render(request, 'networth/starter.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'networth/pages/examples/register.html')
    else:
        username = request.POST.get('email')
        raw_password1 = request.POST.get('password1')
        raw_password2 = request.POST.get('password2')
        fullname = request.POST.get('fullname')
        return redirect('/')


def signup_django(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'networth/signup_dj.html', {'form': form})