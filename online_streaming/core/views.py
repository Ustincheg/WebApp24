from django.views.generic.list import ListView
from .models import Films, Genre, Country
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator

class FilmView(ListView):
    template_name = 'index.html'
    queryset = Films.objects.order_by('?')
    context_object_name = 'items'
    paginate_by = 18

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['genre'] = Genre.objects.all()
        context['country'] = Country.objects.all()
        return context
    
    
    def get_queryset(self) :
        return super().get_queryset()


def film(request, kinopoisk_id):  
    film_item = Films.objects.get(kinopoisk_id=kinopoisk_id)  
    return render(request, 'detail_film.html', {'item': film_item})


class Search(ListView):
    paginate_by = 18
    model = Films
    template_name = 'index.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
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
            data = list(query.values())
            return JsonResponse({'context': data}, status=200)
