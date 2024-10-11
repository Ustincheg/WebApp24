document.addEventListener('DOMContentLoaded', function () {
    // Получаем все элементы списка жанров и стран
    const genreItems = document.querySelectorAll('.menu-genre li');
    const countryItems = document.querySelectorAll('.menu-country li');
    const searchInput = document.querySelector('.search-bar');  // Поле для поиска по названию

    // Функция для выполнения AJAX-запроса
    function fetchFilms(selectedGenre, selectedCountry, searchQuery) {
        const url = '/filter/';  // Указываем правильный URL для фильтрации

        // Формируем URL с параметрами поиска, жанра и страны
        const params = new URLSearchParams();
        if (selectedGenre) {
            params.append('genre', selectedGenre);
        }
        if (selectedCountry) {
            params.append('country', selectedCountry);
        }
        if (searchQuery) {
            params.append('q', searchQuery);
        }

        // Выполняем AJAX-запрос с параметрами
        fetch(`${url}?${params.toString()}`, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest'  // Проверяем, что запрос AJAX
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.context);  // Выводим данные фильмов в консоль для проверки

            // Обновляем список фильмов в секции "shows-list"
            const showsList = document.querySelector('.shows-list');
            showsList.innerHTML = '';  // Очищаем предыдущие фильмы

            if (data.context.length > 0) {
                data.context.forEach(film => {
                    const filmCard = `
                        <div class="show-card">
                            <a href="/${film.kinopoisk_id}/" class="card-link"></a>  
                            <img src="${film.image_url}" alt="${film.title}">
                            <h3>${film.title}</h3>
                            <p>${film.years}</p>
                        </div>`;
                    showsList.insertAdjacentHTML('beforeend', filmCard);  // Добавляем новые фильмы в секцию
                });
            } else {
                // Если фильмов нет, выводим сообщение
                showsList.innerHTML = '<p>Фильмы не найдены для выбранных параметров.</p>';
            }
        })
        .catch(error => {
            console.error('Ошибка при загрузке фильмов:', error);
        });
    }

    let selectedGenre = '';  // Для хранения выбранного жанра
    let selectedCountry = '';  // Для хранения выбранной страны

    // Обрабатываем клик по каждому элементу списка жанров
    genreItems.forEach(item => {
        item.addEventListener('click', function () {
            selectedGenre = this.textContent.trim();  // Получаем название жанра и убираем пробелы
            const searchQuery = searchInput.value.trim();    // Получаем текущий поисковый запрос

            // Выполняем запрос с текущими параметрами
            fetchFilms(selectedGenre, selectedCountry, searchQuery);
        });
    });

    // Обрабатываем клик по каждому элементу списка стран
    countryItems.forEach(item => {
        item.addEventListener('click', function () {
            selectedCountry = this.textContent.trim();  // Получаем название страны и убираем пробелы
            const searchQuery = searchInput.value.trim();    // Получаем текущий поисковый запрос

            // Выполняем запрос с текущими параметрами
            fetchFilms(selectedGenre, selectedCountry, searchQuery);
        });
    });

});
