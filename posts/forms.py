from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from django import forms
from dal import autocomplete

from django.forms import ModelForm
from .models import Post
from tags.models import Tag


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete'),
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'sponsored', 'published', 'image_field', 'tags']
        labels = {
            "title": "Tytuł",
            "content": "Treść",
            "published": "Opublikowany",
            "sponsored": "Sponsorowany",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'contact'
        self.helper.layout = Layout(
            Fieldset(
                'Dodaj post',
                'title',
                'content',
                'published',
                'sponsored',
                'image_field',
                'tags',
            ),
            ButtonHolder(
                Submit('submit', 'Dodaj', css_class='btn btn primary'),
                css_class="d-flex justify-content-end"
            )
        )


class AllPostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
