from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Game(models.Model):
    """
    Game Model

    Attributes:
    - ID
    - Name
    """
    name = models.CharField(max_length=50)


class Player(models.Model):
    """
    Player model

    Attributes:
     - ID
     - Username
     - Team
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(
        Game, on_delete=models.PROTECT, null=True, default=None)


@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()
