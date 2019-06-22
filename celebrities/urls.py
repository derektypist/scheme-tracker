from django.conf.urls import url
from .views import celebrities

urlpatterns = [
    url(r'^$', celebrities, name='celebrities')
    ]
