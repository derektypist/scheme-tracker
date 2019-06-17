from django.shortcuts import render

def denonstrations(request):
    """ Render the demonstrations page """
    return render(request, "demonstrations.html")