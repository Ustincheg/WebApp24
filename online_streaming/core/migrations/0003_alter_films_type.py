# Generated by Django 5.1.2 on 2024-10-13 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_films_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='type',
            field=models.CharField(choices=[('Фильмы', 'Фильмы'), ('Сериалы', 'Сериалы')], max_length=255, verbose_name='Тип фильма'),
        ),
    ]
