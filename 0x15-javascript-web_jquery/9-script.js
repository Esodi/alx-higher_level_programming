$(document).ready(function(){
	$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data, status) {
		let n = data.hello;
		$('#hello').text(n);
	});
});
