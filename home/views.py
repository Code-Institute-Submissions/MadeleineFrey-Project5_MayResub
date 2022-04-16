from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Team, Location, Contact
# Create your views here.

def index(request):
    """ A view to return the index/home page """

    return render(request, 'home/index.html')

def team(request):
    """ A view to """
    xteam = Team.objects.all()
    xlocation = Location.objects.all()
    xcontact = Contact.objects.all()
    
    context = {
        'xteam': xteam,
        'xlocation': xlocation,
        'xcontact': xcontact

    }

    return render(request, 'home/about_us.html', context)