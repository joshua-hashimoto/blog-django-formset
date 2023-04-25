from datetime import datetime as dt

from django import forms

from .models import Author, Book


def validate_date_is_before_today(value):
    today = dt.now()
    if today.date() <= value:
        raise forms.ValidationError("今日より前に設定してください。")
    return value


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = (
            "name",
            "birthday",
        )

    def clean_birthday(self):
        cleaned_data = self.cleaned_data
        birthday = cleaned_data.get("birthday", None)
        return validate_date_is_before_today(birthday)


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = (
            "name",
            "published",
            "rate",
        )

    def clean_published(self):
        cleaned_data = self.cleaned_data
        published = cleaned_data.get("published", None)
        return validate_date_is_before_today(published)


class BookBaseFormset(forms.BaseInlineFormSet):
    def get_filled_forms(self, forms):
        filtered = filter(lambda form: form.cleaned_data.get("name"), forms)
        return list(filtered)

    def get_names(self, forms):
        names = map(lambda form: form.cleaned_data.get("name"), forms)
        return list(names)

    def clean(self):
        filtered_forms = self.get_filled_forms(self.forms)
        names = self.get_names(filtered_forms)
        has_same_book_name = len(set(names)) == 1 and len(filtered_forms) > 1
        if has_same_book_name:
            raise forms.ValidationError("同じタイトルの本が存在するようです。")


BookFormset = forms.inlineformset_factory(
    Author,
    Book,
    form=BookForm,
    formset=BookBaseFormset,
    can_delete=True,
    extra=3
)
