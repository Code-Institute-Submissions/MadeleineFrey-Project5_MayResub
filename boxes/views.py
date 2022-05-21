from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Box, Category
from .forms import BoxForm

# Create your views here.


def all_boxes(request):
    """ A view to show all products """
    boxes = Box.objects.all()
    category = None

    if 'category' in request.GET:
        category = request.GET['category']

        categories = request.GET['category'].split(',')
        boxes = boxes.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    context = {
        'boxes': boxes,
    }

    return render(request, 'boxes/boxes.html', context)


def detail_box(request, box_id):
    """ A view to show individual Box details """

    box = get_object_or_404(Box, pk=box_id)

    context = {
        'box': box,
    }

    return render(request, 'boxes/detail_box.html', context)


@login_required
def add_box(request):
    """ Add a box to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BoxForm(request.POST, request.FILES)
        if form.is_valid():
            box = form.save()
            messages.success(request, 'Successfully added box!')
            return redirect(reverse('box_detail', args=[box.id]))
        else:
            messages.error(request, 'Failed to add box. Please ensure the form is valid.')  # noqa: E501
    else:
        form = BoxForm()

    template = 'boxes/add_box.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_box(request, box_id):
    """ Edit a box in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    box = get_object_or_404(Box, pk=box_id)
    if request.method == 'POST':
        form = BoxForm(request.POST, request.FILES, instance=box)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated box!')
            return redirect(reverse('box_detail', args=[box.id]))
        else:
            messages.error(request, 'Failed to update box. Please ensure the form is valid.')  # noqa: E501
    else:
        form = BoxForm(instance=box)
        messages.info(request, f'You are editing {box.name}')

    template = 'boxes/edit_box.html'
    context = {
        'form': form,
        'box': box,
    }

    return render(request, template, context)


@login_required
def delete_box(request, box_id):
    """ Delete a box from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    box = get_object_or_404(Box, pk=box_id)
    box.delete()
    messages.success(request, 'Box deleted!')
    return redirect(reverse('boxes'))
