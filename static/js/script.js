"use strict";
$(document).ready(function(){
	$('body').on('click', 'a', function(event){
		event.preventDefault();
		console.log($(this).attr("href"));
		$.get($(this).attr('href'), function(response){
			console.log("Hey !!!!")	
			console.log(typeof(response));
			$('#initial').css('display', 'none');
			$('a').css('display', 'inline-block');
			$("#result").html(response);
		});
	})
});