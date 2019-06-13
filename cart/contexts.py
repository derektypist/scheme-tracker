from django.shortcuts import get_object_or_404
from schemes.models import Scheme

def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    cart = request.session.get('cart', {})
    
    cart_items = []
    total_cost = 0
    scheme_count = 0
    for id, quantity in cart.items():
        scheme = get_object_or_404(Scheme, pk=id)
        total_cost += quantity * scheme.cost
        scheme_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'scheme': scheme})
        
    return {'cart_items': cart_items, 'total_cost': total_cost, 'scheme_count': scheme_count}    