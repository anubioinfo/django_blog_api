from django.conf.urls import url, include
from django.contrib import admin
from .views import BlogsClass


urlpatterns = [
    url(r'^$',BlogsClass.as_view(), name='blogs')

]