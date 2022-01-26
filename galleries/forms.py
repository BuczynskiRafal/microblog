from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder

from .models import Gallery
from .models import Photo


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('title', 'description')


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("title", 'short_description', 'image')

