from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'sponsored', 'published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'Dodaj'
        self.helper.add_input(Submit('submit', 'Wyślij'))


class AllPostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
