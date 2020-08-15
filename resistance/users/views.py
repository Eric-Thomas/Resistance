from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to login.')

            return redirect('login')

    else:
        form = UserRegisterForm()

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
