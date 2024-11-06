const dropdowns = document.querySelectorAll('.dropdown');
dropdowns.forEach(dropdown => {
  const select = dropdown.querySelector('.select');
  const caret = dropdown.querySelector('.caret');
  const menuGenre = dropdown.querySelector('.menu-genre');
  const menuCountry = dropdown.querySelector('.menu-country');
  const menuType = dropdown.querySelector('.menu-type'); 
  const optionsGenre = dropdown.querySelectorAll('.menu-genre li');
  const optionsCountry = dropdown.querySelectorAll('.menu-country li');
  const optionsType = dropdown.querySelectorAll('.menu-type li'); 
  const selected = dropdown.querySelector('.selected');

  select.addEventListener('click', () => {
    select.classList.toggle('select-clicked');
    caret.classList.toggle('caret-rotate');

    if (menuGenre) {
      menuGenre.classList.toggle('menu-genre-open');
    }

    // Toggle country menu if it exists
    if (menuCountry) {
      menuCountry.classList.toggle('menu-country-open');
    }

    if (menuType) {
      menuType.classList.toggle('menu-type-open'); 
    }
  });


  optionsGenre.forEach(option => {
    option.addEventListener('click', () => {
      selected.innerText = option.innerText;  
      select.classList.remove('select-clicked');
      caret.classList.remove('caret-rotate');
      menuGenre.classList.remove('menu-genre-open');

      optionsGenre.forEach(opt => {
        opt.classList.remove('active');
      });
      option.classList.add('active');
    });
  });

  optionsCountry.forEach(option => {
    option.addEventListener('click', () => {
      selected.innerText = option.innerText;  
      select.classList.remove('select-clicked');
      caret.classList.remove('caret-rotate');
      menuCountry.classList.remove('menu-country-open');


      optionsCountry.forEach(opt => {
        opt.classList.remove('active');
      });
      option.classList.add('active');
    });
  });

  
  optionsType.forEach(option => {
    option.addEventListener('click', () => {
      selected.innerText = option.innerText;  
      select.classList.remove('select-clicked');
      caret.classList.remove('caret-rotate');
      menuType.classList.remove('menu-type-open');

      optionsType.forEach(opt => {
        opt.classList.remove('active');
      });
      option.classList.add('active');
    });
  });
});
