from django.shortcuts import render, redirect
from .forms import GameCreateForm, GameJoinForm
from django.contrib import messages


def root(request):
    """
    Root Route

    Landing page that allows users to create or join room
    """
    forms = {'game_create_form': GameCreateForm(
    ), 'game_join_form': GameJoinForm()}
    return render(request, 'game/index.html', {'forms': forms})


def game(request, name):
    print(request.POST)
    return render(request, 'game/board.html', {'name': name})


def join_game(request, name):
    print(request.POST)
    return render(request, 'game/board.html', {'name': name})
