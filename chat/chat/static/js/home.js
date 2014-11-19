var asdf = 'asdf';


// bind the csrf_token so django can allow post request
var tmp_token = '{% csrf_token %}';
// django stores it as a cookie if it sees a csrf_token in template
var csrf_token = document.cookie.match(/csrftoken=(.*);?/)[1]

// if post is made straing up
$("body").bind("ajaxSend", function(elm, xhr, s){
   if (s.type == "POST") {
      xhr.setRequestHeader('X-CSRF-Token', csrf_token);
   }
});


// if post is made using jquery
$( document ).ajaxSend( function( ev, xhr, settings ) {
    xhr.setRequestHeader( "X-CSRFToken", csrf_token );
});

// event registration
$('#post').click( function(event) {
    var message = $('#message').val();
    // post the value if it exists
    if (message){
        // XXX handle error
        $.post('api/message/POST', data={text:message});
        console.log(message);

    }
});

// load the messages
$.get('/api/message', function (data) {
   console.log(data);
   var messages = data['response_json'];
   $.each(messages, function(index, value) {

      $('#list').append('<li class="list-group-item list-group-item-info">'+ value.text + '</li>');

   });
});
