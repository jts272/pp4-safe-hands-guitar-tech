from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ('image', 'user', 'instrument', 'date_in', 'job_status')
    list_filter = ('job_status',)

    fieldsets = (
        (None, {
            'fields': (
                'image', ('user', 'instrument'), ('date_in', 'job_status'))
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
