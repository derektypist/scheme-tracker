from django.shortcuts import render

def news(request):
    """ Render the news page """
    return render(request, "news.html")