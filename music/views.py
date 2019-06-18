from django.shortcuts import render

def music(request):
    """ Render the music page """
    return render(request, "music.html")
