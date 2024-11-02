
import json
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_streaming.settings')
django.setup()
from core.models import Genre, Country, Films
from online_streaming import settings
def load_data():
    with open('final__1.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for item in data['items']:
        print(item)
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
                'short_description': item['shortDescription'],   
                'image_url': None,
                'years': item['year'],
                'duration': item['filmLength'],
                'budget':item['budget'] if 'budget' in item else None,
                'fees':item['fees'] if 'fees' in item else None,
                'description':item['description'],
                'type': item['type']
            }
        )
        film.genres.set(genres)
        film.country.set(countries)
        film.save()

PATH = "C:/Study/request/film"

def load_image():
    for i in os.listdir(PATH):
        file_path = os.path.join(settings.MEDIA_ROOT + '/images/', i)
        print(file_path)
        id  = i.split('.')[0]
        obj = Films.objects.get(kinopoisk_id = id)
        print(obj)
        obj.image_url = file_path

        obj.save()

load_image()
