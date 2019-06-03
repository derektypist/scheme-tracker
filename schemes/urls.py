from django.conf.urls import url
from .views import get_schemes, scheme_detail, create_or_edit_scheme

urlpatterns = [
    url(r'^$', get_schemes, name='get_schemes'),
    url(r'^(?P<pk>\d+)$', scheme_detail, name='scheme_detail'),
    url(r'^new/$', create_or_edit_scheme, name='new_scheme'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_scheme, name='edit_scheme')
]