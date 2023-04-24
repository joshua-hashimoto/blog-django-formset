from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AuthorForm, BookFormset
from .models import Author, Book


class CreateBookView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "books/forms.html"
    success_url = reverse_lazy("books:create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formset"] = BookFormset(self.request.POST or None)
        context["object_list"] = Author.objects.all()
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context.get("formset", None)

        if formset is None:
            return super().form_invalid(form)

        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response

        return super().form_invalid(form)
