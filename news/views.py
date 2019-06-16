from django.shortcuts import render
from schemes.models import Scheme

def news(request):
    """ Render the news page """
    return render(request, "news.html")