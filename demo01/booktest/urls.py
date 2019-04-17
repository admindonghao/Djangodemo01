from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', index),
    url(r'^list/$', list),
    url(r'^detail/(\d+)/$', detail)
]
