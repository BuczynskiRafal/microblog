from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'created', 'modified', 'sponsored']
    fields = ['title', 'published']
    exclude = ['content']

# admin.site.register(Post)

