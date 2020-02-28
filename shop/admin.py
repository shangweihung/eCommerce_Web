from django.contrib import admin
from .models import Category, Product

#superusername: admin
#password: aa000000

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created_at', 'updated_at']   # add additional fields to the view.
    list_filter = ['category', 'available', 'created_at', 'updated_at']     # filter which items are displayed
    fields = ['category', 'name','slug' ,'description', ('price', 'stock'),  'available','image']  # detail view layout
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
