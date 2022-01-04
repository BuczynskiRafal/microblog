from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Post
from .models import Category


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


@admin.register(Post)
class PostAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['title', 'published', 'created', 'modified', 'sponsored']
    fields = ['title', 'content', 'published', 'sponsored', 'author', 'category', 'file']
    list_filter = ['published', 'sponsored']
    autocomplete_fields = ['tags', ]
    resource_class = PostResource


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

