# Generated by Django 5.1.2 on 2024-10-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_films_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='image_url',
            field=models.ImageField(upload_to='images', verbose_name='Обложка'),
        ),
    ]
