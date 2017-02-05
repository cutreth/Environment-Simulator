from django.conf.urls import url

import views

urlpatterns = [
    url(r'^sync/$', views.sync, name='sync'),
    url(r'^chart/$', views.chart, name='chart'),
]
