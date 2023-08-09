from django.db import models
from src.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Наименование')

    class Meta:
        db_table = "categoryes"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)


class Tag(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Наименование')

    class Meta:
        db_table = "tags"
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ("name",)


class Product(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products',
                                 verbose_name='Категория')
    tags = models.ManyToManyField(Tag, related_name='products',
                                 verbose_name='Теги')

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("name",)
