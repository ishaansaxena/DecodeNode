from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import UserData
from .forms import  RegistrationForm, UserEditForm, UserProfileForm
from decode.views import index

@login_required
def profile(request):
    current_user = User.objects.get(id=request.user.id)
    top = UserData.objects.order_by('-current_level', 'current_level_time')
    rank = list(top).index(User.objects.get(username=request.user.username).details) + 1
    context = {
        'user': current_user,
        'user_rank': rank,
        'form': '',
    }
    if request.method == 'GET':
        return render(request, 'accounts/profile.html', context)
    else:
        return render(request, 'accounts/profile.html', context)

def peer_profile(request, profile_username):
    if profile_username == request.user.username:
        return redirect('accounts:profile')
    viewed_user = User.objects.get(username=profile_username)
    top = UserData.objects.order_by('-current_level', 'current_level_time')
    rank = list(top).index(User.objects.get(username=request.user.username).details) + 1
    context = {
        'user': viewed_user,
        'user_rank': rank
    }
    if request.method == 'GET':
        return render(request, 'accounts/profile.html', context)
    else:
        return render(request, 'accounts/profile.html', context)


def leaderboard(request):
    top = UserData.objects.order_by('-current_level', 'current_level_time')[:]
    top_classes = ['first topten', 'second topten', 'third topten'] + ['topten'] * 7 + [''] * (len(top) - 10)
    leaderboard = zip(top, top_classes)
    context = {
        'leaderboard': leaderboard,
    }
    print leaderboard
    if request.user.is_authenticated():
        rank = list(top).index(User.objects.get(username=request.user.username).details) + 1 
        context['user_rank'] = rank
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
