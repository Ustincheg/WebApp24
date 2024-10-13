const dropdowns = document.querySelectorAll('.dropdown');
dropdowns.forEach(dropdown => {
  const select = dropdown.querySelector('.select');
  const caret = dropdown.querySelector('.caret');
  const menuGenre = dropdown.querySelector('.menu-genre');
  const menuCountry = dropdown.querySelector('.menu-country');
  const menuType = dropdown.querySelector('.menu-type'); // New menu-type
  const optionsGenre = dropdown.querySelectorAll('.menu-genre li');
  const optionsCountry = dropdown.querySelectorAll('.menu-country li');
  const optionsType = dropdown.querySelectorAll('.menu-type li'); // Options for menu-type
  const selected = dropdown.querySelector('.selected');

  // Handle click on the select element to toggle the menu and caret
  select.addEventListener('click', () => {
    select.classList.toggle('select-clicked');
    caret.classList.toggle('caret-rotate');

    // Toggle genre menu if it exists
    if (menuGenre) {
      menuGenre.classList.toggle('menu-genre-open');
    }

    // Toggle country menu if it exists
    if (menuCountry) {
      menuCountry.classList.toggle('menu-country-open');
    }

    // Toggle type menu if it exists
    if (menuType) {
      menuType.classList.toggle('menu-type-open'); // New menu-type toggle
    }
  });

  // Handle selecting an option from the genre menu
  optionsGenre.forEach(option => {
    option.addEventListener('click', () => {
      selected.innerText = option.innerText;  // Set the selected text
      select.classList.remove('select-clicked');
      caret.classList.remove('caret-rotate');
      menuGenre.classList.remove('menu-genre-open');

      // Remove active class from all genre options and add to the clicked one
      optionsGenre.forEach(opt => {
        opt.classList.remove('active');
      });
      option.classList.add('active');
    });
  });

  // Handle selecting an option from the country menu
  optionsCountry.forEach(option => {
    option.addEventListener('click', () => {
      selected.innerText = option.innerText;  // Set the selected text
      select.classList.remove('select-clicked');
      caret.classList.remove('caret-rotate');
      menuCountry.classList.remove('menu-country-open');

      // Remove active class from all country options and add to the clicked one
      optionsCountry.forEach(opt => {
        opt.classList.remove('active');
      });
      option.classList.add('active');
    });
  });

  
  optionsType.forEach(option => {
    option.addEventListener('click', () => {
      selected.innerText = option.innerText;  // Set the selected text
      select.classList.remove('select-clicked');
      caret.classList.remove('caret-rotate');
      menuType.classList.remove('menu-type-open'); // Close the type menu

      // Remove active class from all type options and add to the clicked one
      optionsType.forEach(opt => {
        opt.classList.remove('active');
      });
      option.classList.add('active');
    });
  });
});
