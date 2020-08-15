from django.db import models


class Game(models.Model):
    """
    Game Model

    Attributes:
    - ID
    - Name
    """
    name = models.CharField(max_length=50)
