$.get('https://swapi.co/api/people/5/?format=json', function (data, status) {
  $('div#character').text(data.name);
});
