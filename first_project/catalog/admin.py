from django.contrib import admin
from .models import Category, Goods, Tag, Parametr
import admin_thumbnails
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin


class CategoryAdmin(DraggableMPTTAdmin):
    # list_display = ['id', 'name', 'activate', 'created', 'updated', 'email']
    list_filter = ['activate']
    search_fields = ['name']


@admin_thumbnails.thumbnail('image')
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activate', 'created', 'category', 'image_thumbnail']
    list_display_links = ['name']
    list_filter = ['activate', 'category']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Tag)
admin.site.register(Parametr)


