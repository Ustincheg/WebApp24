from django.views.generic.list import ListView
from .models import Films, Genre, Country, Watch_later, Comments
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import Comment
from django.core.exceptions import PermissionDenied


class FilmView(ListView):
    template_name = 'index.html'
    queryset = Films.objects.order_by('?')
    context_object_name = 'items'
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = Genre.objects.all()
        context['country'] = Country.objects.all()
        return context

    def get_queryset(self):
        return super().get_queryset()


@login_required
def Film_watch(request):
    obj = Watch_later.objects.prefetch_related('film').get(user=request.user)
    return render(request, 'films_watch.html', {'items': obj.film.all()})

def film(request, kinopoisk_id):
    comments = Comments.objects.none()  
    try:
        film_item = Films.objects.get(kinopoisk_id=kinopoisk_id)
        comments = Comments.objects.filter(film=film_item)
    except Films.DoesNotExist:
        pass
    
    watch = 'Смотреть позже'    
    if request.user.is_authenticated:    
        if Watch_later.objects.filter(user=request.user, film=film_item).exists():
            watch = "Убрать из списка"
        else:
            watch = "Смотреть позже"

    return render(request, 'detail_film.html', {'item': film_item, 'watch': watch, 'comments': comments})


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
        url_parameter = request.GET.get('q', '')
        genre = request.GET.get('genre', '')
        country = request.GET.get('country', '')
        type = Films.get_type(request.GET.get('type', ''))

        if type:
            query = query.filter(type=type)
        if url_parameter:
            query = query.filter(title__istartswith=url_parameter)
        if genre:
            query = query.filter(genres__name=genre)
        if country:
            query = query.filter(country__name=country)

    return query


def Filtr(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'GET':
            query = Films.objects.all()
            query = filter_films(request, query)
            data = [
                {
                    'kinopoisk_id': film.kinopoisk_id,
                    'title': film.title,
                    'years': film.years,
                    'get_image_url': film.get_image_url
                }
                for film in query
            ]
            return JsonResponse({'context': data}, status=200)


def search_navbar(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'GET':
            query = request.GET.get('q', '')
            films = Films.objects.filter(title__istartswith=query)[:5] if query else Films.objects.none()
            data = [
                {
                    'kinopoisk_id': film.kinopoisk_id,
                    'title': film.title,
                    'years': film.years,
                    'get_image_url': film.get_image_url
                }
                for film in films
            ]
            return JsonResponse({'context': data}, status=200)


def watch_later(request, kinopoisk_id):
    if request.user.is_authenticated:
        try:
            film = Films.objects.get(kinopoisk_id=kinopoisk_id)
            obj, created = Watch_later.objects.get_or_create(user=request.user)
            if film in obj.film.all():
                obj.film.remove(film)
            else:
                obj.film.add(film)
        except Films.DoesNotExist:
            pass

    return redirect('film', kinopoisk_id=kinopoisk_id)

@login_required
def add_comment(request, kinopoisk_id):
    film = get_object_or_404(Films, kinopoisk_id=kinopoisk_id)    
    if request.method == 'POST':
        form = Comment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.film = film
            comment.user = request.user
            comment.save()
            return redirect('film', kinopoisk_id=kinopoisk_id) 
    else:
        form = Comment()
    return render(request, 'detail_film.html', {"form":form, 'item':film})


@login_required
def remove_comment(request, kinopoisk_id, comment_id):
    comment = get_object_or_404(Comments, pk = comment_id)
    if comment.user != request.user:
        raise PermissionDenied("Вы можете удалять только свои комментарии.")
    else:
        comment.delete()
        return redirect('film', kinopoisk_id=kinopoisk_id)

