from django import forms
from .models import Game


class GameCreateForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'name'
        ]


class GameJoinForm(forms.Form):
    name = forms.CharField(label='Game', max_length=50)
