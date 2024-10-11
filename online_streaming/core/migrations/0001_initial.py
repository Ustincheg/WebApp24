# Generated by Django 5.1.1 on 2024-10-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название фильма')),
                ('short_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Короткое описание')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание фильма')),
                ('kinopoisk_id', models.PositiveIntegerField(verbose_name='ID в кинопоиске')),
                ('image_url', models.URLField(verbose_name='Url на обложку')),
                ('years', models.PositiveIntegerField(verbose_name='Год выпуска')),
                ('fees', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Сборы')),
                ('budget', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Бюджет фильма')),
                ('grade', models.DecimalField(decimal_places=1, default=0, max_digits=3, max_length=10, verbose_name='Оценка фильма')),
                ('duration', models.PositiveIntegerField(verbose_name='Продолжительность фильма')),
                ('type', models.CharField(max_length=255, verbose_name='Тип фильма')),
                ('country', models.ManyToManyField(to='core.country', verbose_name='Страна')),
                ('genres', models.ManyToManyField(to='core.genre', verbose_name='Жанры')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]
