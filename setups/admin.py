from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'instrument', 'date_in',
                    'job_status', 'public_status')
    list_filter = ('job_status', 'public_status')

    fieldsets = (
        (None, {
            'fields': (
                'image', ('user', 'instrument'), ('date_in', 'job_status',),
                'public_status')
        }),
        ('Initial specification', {
            'fields': ('pre_string_brand',
                       'pre_string_gauges',
                       'pre_scale_length',
                       'pre_fretboard_radius',
                       'pre_bridge_saddle_radius',
                       'pre_fret_width_and_height',
                       'pre_neck_relief',
                       'pre_nut_action',
                       'pre_action_1',
                       'pre_action_2',
                       'pre_action_3',
                       'pre_neck_pickup_height',
                       'pre_middle_pickup_height',
                       'pre_bridge_pickup_height',
                       'pre_notes',
                       )
        }),
        ('Completed specification', {
            'fields': ('post_string_brand',
                       'post_string_gauges',
                       'post_scale_length',
                       'post_fretboard_radius',
                       'post_bridge_saddle_radius',
                       'post_fret_width_and_height',
                       'post_neck_relief',
                       'post_nut_action',
                       'post_action_1',
                       'post_action_2',
                       'post_action_3',
                       'post_neck_pickup_height',
                       'post_middle_pickup_height',
                       'post_bridge_pickup_height',
                       'post_notes',
                       )
        }),
        ('Transaction information', {
            'fields': (('payment_method', 'payment_status'), 'date_out')
        }),
    )

    actions = ('set_visible', 'set_hidden')

    def set_visible(self, request, queryset):
        # Set Job status to visible
        queryset.update(public_status=1)

    def set_hidden(self, request, queryset):
        # Set Job status to visible
        queryset.update(public_status=0)


admin.site.register(Job, JobAdmin)
