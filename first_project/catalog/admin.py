from django.contrib import admin
from .models import Category, Goods, Tag
import admin_thumbnails


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activate', 'created', 'updated', 'email']
    list_filter = ['activate']
    search_fields = ['name']


@admin_thumbnails.thumbnail('image')
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activate', 'created', 'category']
    list_filter = ['activate', 'category']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Tag)

