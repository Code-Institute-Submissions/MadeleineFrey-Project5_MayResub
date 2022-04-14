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
        'stripe_public_key': 'pk_test_51KcqisEb2H0JTspUfup4q1O5OEBTaQ36mkdnjciTiRhZr8N8eP6ND8DU8puW08OKFj1GNW9PmJbrQEnrpp50wdvX00xNngRlDs',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)