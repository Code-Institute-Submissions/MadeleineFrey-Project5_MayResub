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
    """ Add a team member to the store """
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
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')  # noqa: E501
    else:
        form = TeamForm()

    template = 'home/add_team.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_location(request):
    """ Add a location to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('about_us'))

    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            xlocation = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('about_us'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')  # noqa: E501
    else:
        form = LocationForm()

    template = 'home/add_location.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_contact(request):
    """ Add a contact information to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('about_us'))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            xcontact = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('about_us'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')  # noqa: E501
    else:
        form = ContactForm()

    template = 'home/add_contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_team(request, member_id):
    """ Edit a box in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    member = get_object_or_404(Team, pk=member_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated box!')
            return redirect(reverse('about_us'))
        else:
            messages.error(request, 'Failed to update box. Please ensure the form is valid.')  # noqa: E501
    else:
        form = TeamForm(instance=member)
        messages.info(request, f'You are editing {member.name}')

    template = 'home/edit_team.html'
    context = {
        'form': form,
        'member': member,
    }

    return render(request, template, context)


@login_required
def edit_location(request, location_id):
    """ Edit a box in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    location = get_object_or_404(Location, pk=location_id)
    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES, instance=location)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated box!')
            return redirect(reverse('about_us'))
        else:
            messages.error(request, 'Failed to update box. Please ensure the form is valid.')  # noqa: E501
    else:
        form = LocationForm(instance=location)
        messages.info(request, f'You are editing {location.address}')

    template = 'home/edit_location.html'
    context = {
        'form': form,
        'location': location,
    }

    return render(request, template, context)


@login_required
def edit_contact(request, member_id):
    """ Edit a box in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    member = get_object_or_404(Contact, pk=member_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated box!')
            return redirect(reverse('about_us'))
        else:
            messages.error(request, 'Failed to update box. Please ensure the form is valid.')  # noqa: E501
    else:
        form = ContactForm(instance=member)
        messages.info(request, f'You are editing {member.name}')

    template = 'home/edit_contact.html'
    context = {
        'form': form,
        'member': member,
    }

    return render(request, template, context)


@login_required
def delete_team(request, member_id):
    """ Delete a box from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    member = get_object_or_404(Team, pk=member_id)
    member.delete()
    messages.success(request, 'Team member deleted!')
    return redirect(reverse('about_us'))


@login_required
def delete_location(request, location_id):
    """ Delete a box from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    location = get_object_or_404(Location, pk=location_id)
    location.delete()
    messages.success(request, 'Location deleted!')
    return redirect(reverse('about_us'))


@login_required
def delete_contact(request, member_id):
    """ Delete a box from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    member = get_object_or_404(Contact, pk=member_id)
    member.delete()
    messages.success(request, 'Contact deleted!')
    return redirect(reverse('about_us'))
