from django.shortcuts import render, redirect, reverse

from .forms import OrderForm


def checkout(request):
    """ X """
    
    bag = request.session.get('bag', {})
    if not bag:
        return redirect(reverse('boxes'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)