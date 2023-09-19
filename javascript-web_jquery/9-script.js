$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  success: function(data) {
    $('div#hello').append(data.hello);
  },
});
