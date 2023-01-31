from django.contrib import admin
from .models import Blogpost

class BlogpostAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'description', 'text', 'publish_date')

admin.site.register(Blogpost, BlogpostAdmin)
