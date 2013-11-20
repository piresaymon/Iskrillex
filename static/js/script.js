var typeGroup = document.getElementById("typeGroup");
music.addEventListener("click", function () {
  typeGroup.value = "music";
  music.className = music.className.replace("disabled", " ");
  $("#music").addClass("btn-primary");
  $("#picture").addClass("disabled");
  picture.className = picture.className.replace("btn-primary", " ");
  $("#file").addClass("disabled");
  file.className = file.className.replace("btn-primary", " ");
  $("#video").addClass("disabled");
  video.className = video.className.replace("btn-primary", " ");
});
var picture = document.getElementById("picture");
picture.addEventListener("click", function(){
  typeGroup.value = "picture";
  picture.className = picture.className.replace("disabled", " ");
  $("#picture").addClass("btn-primary");
  $("#music").addClass("disabled");
  music.className = music.className.replace("btn-primary", " ");
  $("#file").addClass("disabled");
  file.className = file.className.replace("btn-primary", " ");
  $("#video").addClass("disabled");
  video.className = video.className.replace("btn-primary", " ");
});

var file = document.getElementById("file");
file.addEventListener("click", function(){
  typeGroup.value = "file";
  file.className = file.className.replace("disabled", " ");
  $("#file").addClass("btn-primary");
  $("#music").addClass("disabled");
  music.className = music.className.replace("btn-primary", " ");
  $("#picture").addClass("disabled");
  picture.className = picture.className.replace("btn-primary", " ");
  $("#video").addClass("disabled");
  video.className = video.className.replace("btn-primary", " ");
});

var video = document.getElementById("video");
video.addEventListener("click", function(){
  typeGroup.value = "video";
  video.className = video.className.replace("disabled", " ");
  $("#video").addClass("btn-primary");
  $("#music").addClass("disabled");
  music.className = music.className.replace("btn-primary", " ");
  $("#picture").addClass("disabled");
  picture.className = picture.className.replace("btn-primary", " ");
  $("#file").addClass("disabled");
  file.className = file.className.replace("btn-primary", " ");
});

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

    var $type = $("#typeGroup");
    var $q = $("#q").val().trim();		
	if($type != null & $q.length > 0){
		$form.submit();
	}else{
		alert("Selecione alguma opcao para realizar pesquisa.");
		return false;		
	}
 });
