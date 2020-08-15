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
            game_name = create_form.cleaned_data.get('name')
            messages.success(request, f'Game {game_name} created!')
            return redirect("game", name=game_name)
    else:
        create_form = GameForm()
    return render(request, 'game/index.html', {'create_form': create_form})


def game(request, name):
    return render(request, 'game/board.html', {'name': name})
