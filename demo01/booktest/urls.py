from django.conf.urls import url
from .views import *
urlpatterns = [
    # url(r'index/', index),
    # url(r'index/$', index),
    url(r'$', index),
    url(r'^list/$', list)
]

