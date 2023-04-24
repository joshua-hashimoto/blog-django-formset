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
    def map_rates(self, form):
        rate = form.cleaned_data.get("rate")
        return rate

    def clean(self):
        rates = map(self.map_rates, self.forms)
        is_all_same_values = len(list(set(rates))) == 1
        if is_all_same_values:
            raise forms.ValidationError("全て同じ評価にはできません。")


BookFormset = forms.inlineformset_factory(
    Author,
    Book,
    form=BookForm,
    formset=BookBaseFormset,
    fields=("name", "published", "rate",),
    can_delete=True,
    extra=3
)
