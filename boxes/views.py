from django.shortcuts import render
from .models import Box

# Create your views here.

def all_boxes(request):
    """ A view to show all products """
    boxes = Box.objects.all()
    context = {
        'boxes': boxes,
    }

    return render(request, 'boxes/boxes.html', context)