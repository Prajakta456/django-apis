from django.conf.urls import re_path
from MessageApp import views 



urlpatterns=[
   re_path(r'^messages/',views.messageApi),
   re_path(r'^messageDetails/(?P<pk>[0-9]+)$', views.message_detail),
]