from django.contrib import admin
from .models import orders, order_items
# Register your models here.

admin.site.register(orders)
admin.site.register(order_items)
