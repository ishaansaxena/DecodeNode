from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    current_user = User.objects.get(id=request.user.id)
    if request.method == 'GET':
        return render(request, 'accounts/profile.html', {'user': current_user})
    else:
        pass

def leaderboard(request):
    top = User.objects.extra(select={"level":"COALESCE(current_level.uid, current_level_time)"}, order_by=["-current_price"])[:]
    return render(request, 'accounts/leaderboard.html', {'leaderboard': top})


def register(request):
    context = {}
    return render(request, 'accounts/register.html', context)
