from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Box

# Create your views here.


def all_boxes(request):
    """ A view to show all products """
    boxes = Box.objects.all()
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