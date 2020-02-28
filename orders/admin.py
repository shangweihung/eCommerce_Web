from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    rwaw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','address','postal_code','city','paid','created', 'updated'] # add additional fields to the view.
    list_filter = ['paid', 'created', 'updated']  # filter which items are displayed
    inlines = [ OrderItemInline]


admin.site.register(Order, OrderAdmin)

