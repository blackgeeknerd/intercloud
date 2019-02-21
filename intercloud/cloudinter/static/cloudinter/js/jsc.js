// JavaScript Document
$(document).ready (function(){
	$('#exampleModal').modal('show') ;
		$('#forsale').click(function(){
		$.ajax({
			   type: "POST",
			   url:  "sq.php",
			   data: {text: $(this).val()}
			   });
		
	});	
				 
$('#subimage img').on({
 mouseover: function (){
	 $(this).css({
				  'cursor' : 'pointer' ,
				  'border-color' : 'purple'
				  });
	 },	
	 mouseout: function (){
	 $(this).css({
				  'cursor' : 'default' ,
				  'border-color' : 'black'
				  });
	 },
	 click: function(){
		 var imageurl = $(this).attr('src');
		 $('#mainimage').fadeOut(30, function(){
											   
          $(this).attr('src', imageurl);
		  }).fadeIn(30) ;
		 
		 
		 }
});

$('#detdown').click(function(){
 $('#detdown').hide() ;
 $('#pdet').show () ;
 $('#detup').show() ;
 $('#desc').hide (300) ;
});
$('#detup').click(function(){
  $('#pdet').hide() ;						   
  $('#pdet2').show() ;
  $('#detup').hide() ;
  $('#detdown').show() ;
 $('#desc').show (300) ;
});

$('#locdown').click(function(){
 $('#locdown').hide() ;
 $('#locdet').show () ;
 $('#locup').show() ;
 $('#locdesc').hide (300) ;
});

$('#locup').click(function(){
  $('#locdet').hide() ;						   
  $('#locdet2').show() ;
  $('#locup').hide() ;
  $('#locdown').show() ;
 $('#locdesc').show (300) ;
});

$('#mapclick').click(function(){
  $('#locdesc').hide () ;
  $('#map').show();
});

$('#loc').click(function(){
  $('#map').hide () ;
  $('#locdesc').show();
  
});

$('#detail').click(function(){
  $('#map1').hide () ;
  $('#detail1').show();
  
});
$('#map').click(function(){
  $('#detail1').hide();
   $('#map1').show () ;
});

		 
 $('#agent').change(function(){
 var selectedvalue = $('#agent option:selected');
 if(selectedvalue.val() == 'Agent' ){
 
	 $('.agent').show() ;
	 
 }
 

}) ;



	});
