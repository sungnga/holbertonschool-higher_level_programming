$.get('https://swapi.co/api/films/?format=json', function (films, status) {
  const data = films.results;
  for (const item of data) {
    $('ul#list_movies').append('<li>' + item.title + '</li>');
  }
});
