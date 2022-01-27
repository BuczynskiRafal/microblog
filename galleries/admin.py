from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from galleries.models import Gallery
from galleries.models import Photo


class GalleryResource(resources.ModelResource):
    class Meta:
        model = Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'created', 'modified', 'status']


class PhotoResource(resources.ModelResource):
    class Meta:
        model = Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'image', 'gallery', 'created', 'modified', 'source', 'status',]

