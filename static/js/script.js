$('a#email').hide(0);
  $('a#software').hide(0);
  $('a#down').hide(0);
  
  $(function(){
  $('a#sd').click(function() {
  $('a#email').fadeIn(200, function() {
  		});
	});
	});
  $(function(){
  $('a#email').mouseout(function() {
  	$('a#email').fadeOut(200)
  	});
  });
  
  $(function(){
  	$('a#sr').mouseover(function(){
		$('a#down').fadeIn(200);
	});
  });
  $(function(){
  	$('a#sr').mouseout(function(){
		$('a#down').fadeOut(100);
	});
  });

 $("#submitButton").click(function(event) {
    event.preventDefault(); 
    var $form = $("#searchForm");        

    var type = $("input:radio[name='typeGroup']").is(":checked");
	//var type = $("input:radio[name='typeGroup']").attr("checked");
	//var type = $("#typeGroup").is(":checked");
    var q = $("#q").val().trim();	
	//if($("#typeGroup").is(":checked") & q.length > 0){
	if(type & q.length > 0){
		$form.submit();
	}else{
		alert("Selecione alguma opcao para realizar pesquisa.");
		return false;
		//$.post( url, $form.serialize());
		
	}
	//else{
	//	$.post( url, $form.serialize());	
	//}
    
 });
