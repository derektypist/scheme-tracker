from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Scheme
from .forms import SchemeForm

def get_schemes(request):
    """ 
    Create a view that will return a list of schemes that were published prior to now 
    and render them to the 'schemeposts.html' template
    """

    # Most recent (Published Date) first
    schemes = Scheme.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "schemeposts.html",{'schemes': schemes})

def scheme_detail(request, pk):
    """
    Create a view that returns a single scheme object
    based on the scheme ID (pk) and render it to the 'schemedetail.html' template.
    Or return a 404 error if the scheme is not found.
    """    
    
    scheme = get_object_or_404(Scheme, pk=pk)
    scheme.views += 1
    scheme.save()
    return render(request, "schemedetail.html", {'scheme': scheme})

def create_or_edit_scheme(request, pk=None):
    """
    Create a view that allows us to create or edit a scheme depending
    if the Scheme ID is null or not
    """
    
    scheme = get_object_or_404(Scheme, pk=pk) if pk else None
    if request.method == "POST":
        form = SchemeForm(request.POST, request.FILES, instance=scheme)
        if form.is_valid():
            scheme = form.save()
            return redirect(scheme_detail, scheme.pk)
    else:
        form = SchemeForm(instance=scheme)
        return render(request, "schemeform.html", {'form': form})

def all_schemes(request):
    """
    All Schemes
    """
    schemes = Scheme.objects.all()
    return render(request, "schemeviews.html", {"schemes": schemes})