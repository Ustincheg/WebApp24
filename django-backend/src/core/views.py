from django.views.generic.list import ListView
from .models import Films, Genre, Country, Watch_later
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

class FilmView(ListView):
    template_name = 'index.html'
    queryset = Films.objects.order_by('?')
    context_object_name = 'items'
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['genre'] = Genre.objects.all()
        context['country'] = Country.objects.all()
        return context
    
    def get_queryset(self) :
        return super().get_queryset()


def Film_watch(request):
    obj  = Watch_later.objects.get(user = request.user)
    obj = [i for i in obj.film.all()]
    return render(request, 'films_watch.html', {'items': obj})

def film(request, kinopoisk_id):  
    film_item = Films.objects.get(kinopoisk_id=kinopoisk_id)  
    if film_item.type == 'FIML': 
        return render(request, 'detail_film.html', {'item': film_item})
    else:
        return render(request, 'detail_film.html', {'item': film_item}) 


class Search(ListView):
    paginate_by = 18
    model = Films
    template_name = 'index.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = Genre.objects.all()
        context['country'] = Country.objects.all()
        return context
    
    def get_queryset(self):    
        query = Films.objects.all()
        return filter_films(self.request, query)
        

def filter_films(request, query):
     if request.method == 'GET':
            url_parameter = request.GET.get('q')
            genre = request.GET.get('genre')
            country = request.GET.get('country')    
            type = Films.get_type(request.GET.get('type'))
            if type:
                query = query.filter(type = type)  
            if url_parameter:
                query = query.filter(title__istartswith = url_parameter)
            if genre:
                query = query.filter(genres__name = genre)
            if country:
                query = query.filter(country__name = country)
            return query
     

def Filtr(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  
        if request.method == 'GET':
            query = Films.objects.all()
            query = filter_films(request, query)
            data = []
            for film in query:
                data.append({
                    'kinopoisk_id': film.kinopoisk_id,
                    'title': film.title,
                    'years': film.years,
                    'get_image_url': film.get_image_url 
                })
            return JsonResponse({'context': data}, status=200)

def search_navbar(request):
    if request.headers.get('X-Requested-with') == 'XMLHttpRequest':
        if request.method == 'GET':
            obj = Films.objects.all()
            query = request.GET.get('q', '')
            data = []

            if query:
                obj = obj.filter(title__istartswith = query)[:5]
                for film in obj:
                    data.append({
                        'kinopoisk_id': film.kinopoisk_id,
                        'title': film.title,
                        'years': film.years,
                        'get_image_url': film.get_image_url 
                    })
            return JsonResponse({'context': data}, status=200)
        
def watch_later(request, kinopoisk_id):
    if request.user.is_authenticated:
        temp = Films.objects.get(kinopoisk_id = kinopoisk_id)
        obj, created = Watch_later.objects.get_or_create(user=request.user)
        obj.film.add(temp)
    return redirect('film', kinopoisk_id = kinopoisk_id)