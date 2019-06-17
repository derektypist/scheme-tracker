from django.shortcuts import render

def demonstrations(request):
    """ Render the demonstrations page """
    return render(request, "demonstrations.html")