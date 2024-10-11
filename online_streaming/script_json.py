
import json
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_streaming.settings')
django.setup()
from core.models import Genre, Country, Films
with open('final__1.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
for item in data['items']:
    genres = []
    for genre_data in item['genres']:   
        genre_name = genre_data['genre']
        genre, created = Genre.objects.get_or_create(name=genre_name)
        genres.append(genre)
    countries = []
    for country_data in item['countries']:
        country_name = country_data['country']
        country, created = Country.objects.get_or_create(name=country_name)
        countries.append(country)
    film, created = Films.objects.update_or_create(
        kinopoisk_id=item['kinopoisk_id'],
        defaults={
            'title': item['name'],
            'short_description':item['shortDescription'],
            'image_url': item['url_post'],
            'years': item['year'],
            'duration': item['filmLength'],
            'budget':item['budget'] if 'budget' in item else None,
            'fees':item['fees'] if 'fees' in item else None,
            'description': item['description'],
        }
    )
    film.genres.set(genres)
    film.country.set(countries)
    film.save()
