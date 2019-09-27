$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
  $('div#hello').text(data.hello);
});
