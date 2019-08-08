from django.db import models

DEFAULT_STATUS = 'draft'

STATUS = [
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]

# Create your models here.

class Page(models.Model):
    # title
    title = models.CharField(max_length=200)
    # slug: Bunu arastir!
    slug = models.SlugField(
        max_length=200,
        default='',
        null=True,
        blank=True
    )
    # content
    content = models.TextField()
    # coverimage
    coverimage = models.ImageField(
        upload_to='page',
        null=True,
        blank=True,
        )
    # status
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
    )
    # created at
    created_at = models.DateTimeField(auto_now_add=True)
    # updated at
    updated_at = models.DateTimeField(auto_now=True)


class Carousel(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    cover_image = models.ImageField(
        upload_to='carousel',
        null=True,
        blank=True,
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
