from django.shortcuts import render

def celebrities(request):
    """ Render the celebrities page """
    return render(request, "celebrities.html")
