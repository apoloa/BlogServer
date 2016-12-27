from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.
from blogs.models import Blog


def hello(request):
    return HttpResponse("Hello World")


class BlogList(ListView):
    template = "blogs/blog_list.html"
    queryset = Blog.objects.select_related("owner").annotate(
    ).order_by("name")
