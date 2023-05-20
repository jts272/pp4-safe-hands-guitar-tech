from django.contrib import admin

from .models import Instrument, Job, Order, Product, Setup

# class OrderInline(admin.TabularInline):
#     model = Order


# class ProductInline(admin.TabularInline):
#     model = Product


# class ProductAdmin(admin.ModelAdmin):
#     inlines = [
#         OrderInline
#     ]


# class OrderAdmin(admin.ModelAdmin):
#     inlines = [
#         ProductInline
#     ]


# # Register your models here.
# admin.site.register(Setup)
# admin.site.register(Instrument)

# admin.site.register(Order, OrderAdmin)
# admin.site.register(Product, ProductAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ('image', 'user', 'instrument', 'date_in', 'job_status')
    list_filter = ('job_status',)

    fieldsets = (
        (None, {
            'fields': (('user', 'instrument'), ('date_in', 'job_status'))
        }),
        ('Initial specification', {
            'fields': ('pre_strings',)
        }),
        ('Completed specification', {
            'fields': ('post_strings',)
        }),
        ('Transaction information', {
            'fields': (('payment_method', 'payment_status'), 'date_out')
        }),
    )


admin.site.register(Job, JobAdmin)
