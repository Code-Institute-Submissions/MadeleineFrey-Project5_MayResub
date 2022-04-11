from decimal import Decimal
from django.conf import settings

from django.shortcuts import get_object_or_404
from boxes.models import Box


def bag_contents(request):
    """
    X
    """

    bag_items = []
    total = 0
    box_count = 0
    bag = request.session.get('bag', {})

    for box_id, quantity in bag.items():
        box = get_object_or_404(Box, pk=box_id)
        total += quantity * box.price
        box_count += quantity
        bag_items.append({
            'box_id': box_id,
            'quantity': quantity,
            'box': box,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'box_count': box_count,
        
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'total': total,
        'grand_total': grand_total,
    }

    return context
