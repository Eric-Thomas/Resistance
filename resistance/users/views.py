from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def register(request):

    return render(request, 'users/register.html')


def root(request):
    """ 
    Root Route

    Landing page that allows users to login or register
    """
    return render(request, 'users/index.html')
