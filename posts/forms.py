from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from django import forms

from django.forms import ModelForm
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(label='Tytuł')
    content = forms.CharField(widget=forms.Textarea, label='Treść')
    sponsored = forms.BooleanField(required=False, label='Sponsorowny')
    published = forms.BooleanField(required=False, label='Opublikowany')

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
