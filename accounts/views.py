from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import UserData
from .forms import  RegistrationForm
from decode.views import index

@login_required
def profile(request):
    current_user = User.objects.get(id=request.user.id)
    if request.method == 'GET':
        return render(request, 'accounts/profile.html', {'user': current_user})
    else:
        pass

def leaderboard(request):
    top = UserData.objects.order_by('-current_level', 'current_level_time')
    rank = list(top).index(User.objects.get(username=request.user.username).details) + 1 
    context = {
        'leaderboard': top,
        'user_rank': rank
    }
    return render(request, 'accounts/leaderboard.html', context)

def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = User.objects.create_user(
                email = form.cleaned_data['email'],
                username = form.cleaned_data['username']
            )
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('decode:index')
    return render(request, 'accounts/register.html', {'form': form})
