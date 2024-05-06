$(document).ready(function(){
	$('#toggle_header').click(function(){
		let h = $('header');
		if(h.hasClass('red')) {
			h.removeClass('red').addClass('green');
		}
		else {
			h.removeClass('green').addClass('red');
		}
	});
});
