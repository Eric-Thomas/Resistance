from django.shortcuts import render, redirect
from .forms import GameCreateForm, GameJoinForm
from django.contrib import messages
from .models import Game


def root(request):
    """
    Root Route

    Landing page that allows users to create or join room
    """
    forms = {'game_create_form': GameCreateForm(
    ), 'game_join_form': GameJoinForm()}
    return render(request, 'game/index.html', {'forms': forms})


def game(request):
    name = request.POST.get('name')
    # Create game
    try:
        game = Game(name=name)
        game.save()
        # Query player
        player = Player.objects.get(user=request.user)
        player.game_id = game
        player.save()
    except:
        print("oops")
    # Add player to game
    return render(request, 'game/board.html', {'game': game})


def join_game(request):
    #  Query to see if game exists
    # if exists add to game
    # else send message
    return render(request, 'game/board.html', {'name': request.POST.get('name')})
