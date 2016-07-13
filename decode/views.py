from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Level
from .forms import GameForm


def index(request):
    context = {}
    return render(request, 'decode/index.html', context)

@login_required
def play(request):
    current_user = User.objects.get(username=request.user.username)
    if current_user.details.is_banned:
        return render(request, 'decode/banned.html', {})
    else:
        level = current_user.details.current_level
        form = GameForm(request.POST or None)
        context = {
            'level': level,
            'form': form
        }
        if request.method == 'GET':
            return render(request, 'decode/play.html', context)
        elif request.method == 'POST':
            if form.is_valid():
                if form.cleaned_data['user_answer'] == level.answer:
                    next_level_uid = level.uid + 1
                    current_user.details.current_level = Level.objects.get(pk=next_level_uid)
                    level = current_user.details.current_level
                    current_user.is_banned = True
                    form.save()
                    current_user.save(force_update=True)
                    context['level'] = level
                else:
                    context['errors'] = "Wrong Answer."
                return render(request, 'decode/play.html', context)
            else:
                current_user.details.is_banned = True
                current_user.save()
                return render(request, 'decode/banned.html')