from django.shortcuts import render
from schemes.models import Scheme

# Create your views here.
def do_search(request):
    schemes = Scheme.objects.filter(name__icontains=request.GET['q'])
    return render(request, "schemeposts.html", {"schemes": schemes})