from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from django import forms
from .models import Book
from .models import Borrow


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        # labels = {
        #     "title": "Tytuł",
        #     "content": "Treść",
        #     "published": "Opublikowany",
        #     "sponsored": "Sponsorowany",
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'books:add'
        self.helper.add_input(Submit('submit', 'Wyślij'))


class BookBorrowForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('borrow', 'Wypożycz'))