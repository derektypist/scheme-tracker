from django.conf.urls import url
from .views import demonstrations

urlpatterns = [
    url(r'^$', demonstrations, name='demonstrations')
    ]
