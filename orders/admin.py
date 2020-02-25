from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admim.TabularInline):
    model = OrderItem
    rwaw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','last_name','email','address','postal_code','city','paid','created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [ OrderItemInline]


admin.site.register(Order, OrderAdmin)

