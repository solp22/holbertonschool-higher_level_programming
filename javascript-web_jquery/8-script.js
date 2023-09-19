$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function(data) {
    const movies = data.results
    $.each(movies, function(i, movie) {
      $('ul#list_movies').append('<li>' + movie.title + '</li>');
    });
  },
});