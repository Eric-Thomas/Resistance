from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from django.shortcuts import redirect, render
=======
from django.shortcuts import render
from django.http import HttpResponse
>>>>>>> 6ada6d78db77816e2e0f8b034a0e391656e4e006


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            return redirect('')

    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def root(request):
    """ 
    Root Route

    Landing page that allows users to login or register
    """
    return render(request, 'users/index.html')
