from django.conf.urls import include, url
from django.urls import path

import hello.views

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
]
