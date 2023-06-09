from django.contrib import admin
# Import the models to be accessed in the admin panel
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Post)
# WYSIWYG editor setup: https://youtu.be/er5IKknKxoQ?t=173
class PostAdmin(SummernoteModelAdmin):
    # Declare the fields in the model that will use Summernote editor
    # Further information on use in Django admin:
    # https://github.com/summernote/django-summernote#django-admin-site
    summernote_fields = ('content')
    # Map the slug field match that of the title
    # Django handles the lowercasing and hyphenating via model SlugField
    prepopulated_fields = {'slug': ('title',)}
    # Additional QoL features implemented for admin panel used from:
    # https://youtu.be/JGt1p8JhPyY
    # The fields shown for each post in the list
    list_display = ('title', 'slug', 'status', 'created_on')
    # Search fields to find a post
    search_fields = ('title', 'content')
    # Filter posts by status and creation date
    list_filter = ('status', 'created_on')

    # Actions to bulk-update the display status of blog posts
    actions = (
        'set_selected_posts_as_draft',
        'set_selected_posts_as_published'
    )

    def set_selected_posts_as_draft(self, request, queryset):
        queryset.update(status=0)

    def set_selected_posts_as_published(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Customization of the Comment model fields in the admin panel
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    # Add ability to approve comments from the admin panel
    # Reference: https://youtu.be/JGt1p8JhPyY?t=313
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        # Change the default bool of the approved field to True
        queryset.update(approved=True)
