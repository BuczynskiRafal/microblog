from django import forms

from galleries.models import Gallery
from galleries.models import Photo


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('title', 'description')


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("title", 'short_description', 'status', 'image')

