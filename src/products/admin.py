from django.contrib import admin
from src.products.models import Category, Tag, Product


class ProductInline(admin.StackedInline):
    model = Product
    readonly_fields = ("is_deleted",)
    exclude = ("created_at", "updated_at")
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ("name",)
    list_filter = ("name",)
    readonly_fields = ("id", "is_deleted", "created_at", "updated_at")
    search_fields = ("name",)
    list_per_page = 50
    inlines = [ProductInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ("name",)
    list_filter = ("name",)
    readonly_fields = ("id", "is_deleted", "created_at", "updated_at")
    search_fields = ("name",)
    list_per_page = 50


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_display_links = ("name",)
    list_filter = ("name", 'category')
    readonly_fields = ("id", "is_deleted", "created_at", "updated_at")
    search_fields = ("name",)
    list_per_page = 50
