$(document).ready(function() {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, status) {
        $.each(data.results, function(index, movie) {
            var movieTitle = movie.title;
            var listItem = $('<li>' + movieTitle + '</li>');
            $('#list_movies').append(listItem);
        });
    });
});