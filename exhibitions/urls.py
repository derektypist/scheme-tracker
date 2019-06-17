from django.conf.urls import url
from .views import exhibitions

urlpatterns = [
    url(r'^$', exhibitions, name='exhibitions')
    ]
