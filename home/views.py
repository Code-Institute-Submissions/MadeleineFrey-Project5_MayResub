from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Team, Location, Contact
from .forms import TeamForm, LocationForm, ContactForm
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


@login_required 
def add_team(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            xteam = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = TeamForm()
        
    template = 'home/add_team.html'
    context = {
        'form': form,
    }

    return render(request, template, context)