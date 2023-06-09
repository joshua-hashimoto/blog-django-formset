# Generated by Django 4.2 on 2023-04-23 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('published', models.DateField()),
                ('rate', models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Normal'), (4, 'Good'), (5, 'Very Good')], max_length=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.author')),
            ],
        ),
    ]
