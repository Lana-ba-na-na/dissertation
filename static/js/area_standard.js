$(function(){
	$('#btnArea').click(function(){
		
		$.ajax({
			url: '/prof_standard',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
