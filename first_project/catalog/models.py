from django.db import models
from djrichtextfield.models import RichTextField


class DateTimeStamp(models.Model):
    created = models.DateTimeField('Created', auto_now=True)
    updated = models.DateTimeField('Updated', auto_now_add=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    name = models.CharField('Tag name', max_length=30, unique=True)
    uuid = models.UUIDField('uuid')

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(DateTimeStamp):
    name = models.CharField("Category name", max_length=25, unique=True)
    description = RichTextField("Desc", blank=True)
    url = models.URLField('url', blank=True)
    email = models.EmailField('email', blank=True)
    activate = models.BooleanField('Active', default=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Goods(DateTimeStamp):
    name = models.CharField("Category name", max_length=25, unique=True)
    description = RichTextField("Desc", blank=True)
    price = models.FloatField('Price', default=0)
    activate = models.BooleanField('Active', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goods')
    image = models.ImageField('Image', upload_to='image', blank=True)
    tags = models.ManyToManyField(Tag, related_name="goods_tag")

    class Meta:
        verbose_name = "Goods"
        verbose_name_plural = 'Goods'
        ordering = ['name']

    def __str__(self):
        return self.name
