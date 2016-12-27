# -*- coding: utf-8 -*-

from django.conf.urls import url
from blogs.views import BlogList

urlpatterns = (
    url(r'^blogs/?$', BlogList.as_view(), name="blog_list"),
)