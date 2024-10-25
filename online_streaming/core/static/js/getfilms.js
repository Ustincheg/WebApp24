document.addEventListener('DOMContentLoaded', function () {
    
    const genreItems = document.querySelectorAll('.menu-genre li');
    const countryItems = document.querySelectorAll('.menu-country li');
    const searchInput = document.querySelector('.search-bar'); 
    const typeItems = document.querySelectorAll('.menu-type li')

    function fetchFilms(selectedGenre, selectedCountry, searchQuery, selectedType) {
        const url = '/filter/';  

    
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
        if (typeItems) {
            params.append('type', selectedType)
        }

        fetch(`${url}?${params.toString()}`, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest' 
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.context);  
            
            const showsList = document.querySelector('.shows-list');
            showsList.innerHTML = '';  

            if (data.context.length > 0) {
                data.context.forEach(film => {
                    console.log(film.get_image_url);
                    const filmCard = `
                        <div class="show-card">
                            <a href="/${film.kinopoisk_id}/" class="card-link"></a>  
                            <img src= ${film.get_image_url} >
                            <h3>${film.title}</h3>
                            <p>${film.years}</p>
                        </div>`;
                    showsList.insertAdjacentHTML('beforeend', filmCard);  // Добавляем новые фильмы в секцию
                });
            } else {
                // 
                showsList.innerHTML = '<p>Фильмы не найдены для выбранных параметров.</p>';
            }
        })
        .catch(error => {
            console.error('Ошибка при загрузке фильмов:', error);
        });
    }

    let selectedGenre = '';
    let selectedCountry = ''; 
    let selectedType = ''; 
    
    genreItems.forEach(item => {
        item.addEventListener('click', function () {
            selectedGenre = this.textContent.trim(); 
            const searchQuery = searchInput.value.trim();
            fetchFilms(selectedGenre, selectedCountry, searchQuery, selectedType);
        });
    });

    typeItems.forEach(item => {
        item.addEventListener('click', function(){
            selectedType = this.textContent.trim();
            const searchQuery = searchInput.value.trim();
            fetchFilms(selectedGenre, selectedCountry, searchQuery, selectedType)
        })
    })
    countryItems.forEach(item => {
        item.addEventListener('click', function () {
            selectedCountry = this.textContent.trim();
            const searchQuery = searchInput.value.trim();    

            fetchFilms(selectedGenre, selectedCountry, searchQuery, selectedType);
        });
    });

});
