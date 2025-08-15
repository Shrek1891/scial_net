from django.conf import settings
from django.db import models
from django.utils.text import slugify


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    caption = models.TextField()
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_like', blank=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
