from django.shortcuts import render
from .models import Product

# Define Views
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
