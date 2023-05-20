from django.contrib import admin
from .models import Setup, Instrument, Order, Product


class OrderInline(admin.TabularInline):
    model = Order


class ProductInline(admin.TabularInline):
    model = Product


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline
    ]


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline
    ]


# Register your models here.
admin.site.register(Setup)
admin.site.register(Instrument)

admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
