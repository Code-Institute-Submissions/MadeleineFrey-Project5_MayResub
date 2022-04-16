from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

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

def add_box(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = BoxForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_box'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = BoxForm()
        
    template = 'boxes/add_box.html'
    context = {
        'form': form,
    }

    return render(request, template, context)