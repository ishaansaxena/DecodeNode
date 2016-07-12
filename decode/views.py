from django.shortcuts import render
from .models import Level
from django.contrib.auth.decorators import login_required

def index(request):
    context = {}
    return render(request, 'decode/index.html', context)

@login_required
def play(request):
    if request.user.details.is_banned:
        return render(request, 'decode/banned.html', {})
    else:
        level = request.user.details.current_level
        return render(request, 'decode/play.html', {'level': level})
