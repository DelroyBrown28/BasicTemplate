from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form,
        'stripe_public_key' : 'pk_test_51HX5u6A1fnSIB3Km43MupzPhDdzE3QyyAOUnwsbTnovphUUDBuyIEDZDXo3rNw5SQHBkDuqo3keliCWShvZ3PGdN00gKgCOG4V',
        'client_secret' :  'testing client secret',
        
    }
    
    return render(request, template, context)