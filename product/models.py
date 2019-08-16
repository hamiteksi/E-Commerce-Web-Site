from django.db import models

# Create your models here.

STATUS = [
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]

GENDER_CHOICE = [
    ('man', 'Erkek'),
    ('women', 'Kadin'),
    ('unisex', 'UniSex'),
]

class Category(models.Model):
    title = models.CharField(max_length=30)
    gender = models.CharField(
        default = 'unisex',
        choices=GENDER_CHOICE,
        max_length=10,
    )
    status = models.CharField(
        default = 'draft',
        choices=STATUS,
        max_length=10,
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    product_image = models.ImageField(
        upload_to='product',
        null=True,
        blank=True,
    )
    status = models.CharField(
        default = 'draft',
        choices=STATUS,
        max_length=15

    )
    stock = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
