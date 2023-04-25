from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    RATES = [
        (1, "Very Bad"),
        (2, "Bad"),
        (3, "Normal"),
        (4, "Good"),
        (5, "Very Good"),
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    name = models.CharField(max_length=250)
    published = models.DateField()
    rate = models.IntegerField(choices=RATES)

    def __str__(self):
        return self.name
