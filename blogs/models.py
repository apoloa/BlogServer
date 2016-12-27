from django.contrib.auth.models import User
from django.db import models


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

    def __unicode__(self):
        return self.name
