from django.shortcuts import render, redirect
from .forms import GameCreateForm, GameJoinForm
from django.contrib import messages
from .models import Game, Player


def root(request):
    """
    Root Route

    Landing page that allows users to create or join room
    """
    forms = {'game_create_form': GameCreateForm(
    ), 'game_join_form': GameJoinForm()}
    return render(request, 'game/index.html', {'forms': forms})


def game(request):
    """
    Create Game room
    """
    name = request.POST.get('name')
    # Create game
    try:
        game = Game(name=name)
        game.save()
        # Query player
        player = Player.objects.get(user=request.user)
        player.game_id = game
        player.save()
    except Exception as e:
        print(e)
    # Add player to game
    return render(request, 'game/board.html', {'game': game})


def join_game(request):
    """
    Join Existing Game Room
    """
    #  Query to see if game exists
    name = request.POST.get('name')
    try:
        game = Game.objects.get(name=name)
        player = Player.objects.get(user=request.user)
        player.game_id = game
        player.save()
        return render(request, 'game/board.html', {'game': game})
    except Exception as e:
        print(e)
        messages.warning(request, f'Game {name} does not exist')
        return redirect('/lobby')
