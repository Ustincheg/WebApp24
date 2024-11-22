from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from Users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name= "Жанр")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name= "Страна")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Films(models.Model):
    TYPE_CHOOSE = [
        ("FILM", 'Фильмы'),
        ("TV_SERIES", 'Сериалы')
    ]


    title = models.CharField(max_length=255, verbose_name='Название фильма')
    short_description = models.CharField(max_length=255, verbose_name='Короткое описание', blank=True, null=True)
    description = models.TextField(verbose_name='Описание фильма', blank=True, null=True)
    kinopoisk_id = models.PositiveIntegerField(verbose_name='ID в кинопоиске')
    image_url = models.ImageField(upload_to="images", verbose_name="Обложка")
    years = models.PositiveIntegerField(verbose_name='Год выпуска')
    fees = models.PositiveBigIntegerField(verbose_name='Сборы', blank=True, null=True)
    budget = models.PositiveBigIntegerField(verbose_name='Бюджет фильма', blank=True, null=True)
    country = models.ManyToManyField(Country, verbose_name='Страна')
    grade = models.DecimalField(max_digits=3, decimal_places=1, max_length=5, verbose_name='Оценка фильма', default=0)
    duration = models.PositiveIntegerField(verbose_name='Продолжительность фильма', null= True)
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    type = models.CharField(max_length=255, verbose_name='Тип фильма', choices=TYPE_CHOOSE)

    image_thumbnail = ImageSpecField(source='image_url',
                                     processors=[ResizeToFill(180,270)],
                                     format='JPEG',
                                     options={'quality':85},)
    
    image_large = ImageSpecField(source='image_url',
                                     processors=[ResizeToFill(280,420)],
                                     format='JPEG',
                                     options={'quality':85},)
                                         
    @property
    def get_image_url(self):
        return self.image_thumbnail.url
    

    @classmethod 
    def get_type(cls, type):
        for i in cls.TYPE_CHOOSE:
            if i[1] == type:
                return i[0]
            else:
                continue
        return None 

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Watch_later(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ManyToManyField(Films)
    add_data = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Films, on_delete=models.CASCADE)
    body = models.TextField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True) 
    grade = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    class Meta():
        ordering = ['created_on']