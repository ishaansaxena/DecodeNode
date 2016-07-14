from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserData

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
    context = {}
    return render(request, 'accounts/register.html', context)
