from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Team
# Create your views here.

def index(request):
    """ A view to return the index/home page """

    return render(request, 'home/index.html')

def team(request):
    """ A view to """
    team = Team.objects.all()
    
    context = {
        'team': team,
    }

    return render(request, 'home/about_us.html', context)