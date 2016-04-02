$("#submit-form").click(function(e) {
	$.ajax({
         url : window.location.href, // the endpoint,commonly same url
         type : "POST", // http method
         data : { csrfmiddlewaretoken : csrftoken, 
 	},
 	success : function(json) {
      //console.log(json); // another sanity check
      //On success show the data posted to server as a message
      $("#submit-form").val('');
      alert('Good hash');

 	},
 	error : function(xhr,errmsg,err) {
 		alert(xhr.status + ": " + xhr.responseText);
 	}
})