from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)

from boxes.models import Box

def view_bag(request):
    """
    View renders the bag contents page
    """
    return render(request, "bag/bag.html")

def add_to_bag(request, box_id):
    """ Add a quantity of the specified box to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if box_id in list(bag.keys()):
        bag[box_id] += quantity
    else:
        bag[box_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, box_id):
    """
    Adjust the quantity of a product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[box_id] = quantity
    else:
        bag.pop(box_id)

    request.session['bag'] = bag
    return redirect(reverse('bag'))

def remove_from_bag(request, box_id):
    """ Removes the specified product from the cart """

    try:
        box = get_object_or_404(Box, pk=box_id)
        bag = request.session.get('bag', {})
        bag.pop(box_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)