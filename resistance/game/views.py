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
    name = request.POST.get('name')
    # Create game
    try:
        game = Game(name=name)
        game.save()
        # Query player
        player = Player.objects.get(user=request.user)
        player.game_id = game
        player.save()
        print(player)
    except Exception as e:
        print(e)
    # Add player to game
    return render(request, 'game/board.html', {'game': game})


def join_game(request):
    #  Query to see if game exists
    name = request.POST.get('name')
    game = Game.objects.filter(name=name)
    print(game.count)
    if (game.count() == 0):
        messages.warning(request, f'Game {name} does not exist')
        return redirect('/lobby')
    # if exists add to game
    # else send message
    return render(request, 'game/board.html', {'game': game})
