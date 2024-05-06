$(document).ready(function(){
	$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data, status) {
		let movies = data.results;
		let list = $('#list_movies');
		$.each(movies, function(index, movie){
			list.append('<li>' + movie.title + '</li>');
		});
	});
});
