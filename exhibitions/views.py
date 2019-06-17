from django.shortcuts import render

def exhibitions(request):
    """ Render the exhibitions page """
    return render(request, "exhibitions.html")