from django.core.cache import cache
from django.db import models
from src.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Наименование')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "categoryes"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)


class Tag(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Наименование')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "tags"
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ("name",)


class Product(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products',
                                 verbose_name='Категория')
    tags = models.ManyToManyField(Tag, related_name='products',
                                  verbose_name='Теги', blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, force_insert, force_update, using, update_fields) -> None:
        super().save(force_insert, force_update, using, update_fields)
        cache.clear()
        return None
        

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("name",)
