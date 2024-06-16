$(document).ready(function(){
    $('#userinput').on('keypress', function() {
        var textValue = $(this).val();

        $.ajax({
            url: '/lms/index.html',
            method: 'POST',
            data: {
                'text': textValue
            },
            success: function(response) {
                console.log(response);
            }
        });
    });
});