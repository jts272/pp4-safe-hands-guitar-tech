from django.contrib import admin
# Import the models to be accessed in the admin panel
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Post)
# WYSIWYG editor setup: https://youtu.be/er5IKknKxoQ?t=173
class PostAdmin(SummernoteModelAdmin):
    # Declare the fields in the model that will use Summernote editor
    # Further information on use in Django admin:
    # https://github.com/summernote/django-summernote#django-admin-site
    summernote_fields = ('content')
