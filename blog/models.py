from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category, default=1)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
