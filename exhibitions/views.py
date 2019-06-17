from django.shortcuts import render

def news(request):
    """ Render the exhibitions page """
    return render(request, "exhibitions.html")