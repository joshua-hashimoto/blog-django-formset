from django.urls import path

from .views import CreateBookView

app_name = "books"

urlpatterns = [
    path("", CreateBookView.as_view(), name="create"),
]
