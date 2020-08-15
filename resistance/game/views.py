from django.shortcuts import render, redirect
from .forms import GameForm
from django.contrib import messages


def root(request):
    """
    Root Route

    Landing page that allows users to create or join room
    """
    if request.method == 'POST':
        create_form = GameForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, f'Gamecreated!')
            return redirect("/game", name=request.POST.gameName)
    else:
        create_form = GameForm()
    return render(request, 'game/index.html', {'create_form': create_form})


def game(request, name):
    return render(request, 'game/board.html', {'name': name})
