from django.contrib import admin
# Import the models to be accessed in the admin panel
from .models import Post

# Register your models here.
admin.site.register(Post)
