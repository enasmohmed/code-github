from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.CharField(max_length=100)
    image_author = models.ImageField(upload_to='post/', default='Business-elite-logo-none-bg.png')
    description_author = models.TextField(max_length=1500,blank=True, null=True)
    title = models.CharField(max_length=100)
    tags = TaggableManager(blank=True)
    post_views = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='post/')
    created_at = models.DateTimeField(default=timezone.now)
    description_one = models.TextField(max_length=20000)
    description_two = models.TextField(max_length=20000)
    category = models.ForeignKey(Category, related_name='post_category', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})




