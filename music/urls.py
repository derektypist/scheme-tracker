from django.conf.urls import url
from .views import music

urlpatterns = [
    url(r'^$', music, name='music')
    ]
