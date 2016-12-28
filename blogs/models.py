from django.contrib.auth.models import User
from django.db import models
from wordplease.settings import MEDIA_URL, BASE_URL


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, primary_key=True)

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    owner = models.OneToOneField(User, related_name="blog")
    name = models.CharField(max_length=250)
    description = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    image_name = models.CharField(max_length=250, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_url_image(self):
        return "{}{}{}".format(BASE_URL,MEDIA_URL, self.image_name)
