$(document).ready(function () {

    $('[type="radio"][name="report_type"]').change(function(){
        if(this.checked && this.value=="pivot"){
            $('#pivot-input').fadeIn(this.checked);
            $('#basic-input').fadeOut(this.checked);
        }
        else{
            $('#pivot-input').fadeOut(this.checked);
        }
      
    });
    $('[type="radio"][name="report_type"]').change(function(){
        if(this.checked && this.value=="basic"){
            $('#basic-input').fadeIn(this.checked);
            $('#pivot-input').fadeOut(this.checked);
        }
        else{
            $('#basic-input').fadeOut(this.checked);
        }
      
    });
    $('.ajaxProgress').hide();
    $('#form').submit(function(event){
        
        $('.ajaxProgress').show();
        event.preventDefault();
        $form = $(this);
        var formData = new FormData(this);
        $.ajax({
            data: formData,
            type: 'POST',
            url: '',
            success: function(response){
                console.log(response);
                if (response['success']){
                    $('#form').html('');
                    $('#output').html('<div class="alert alert-success">Successfully uploaded</div>');
                    
                    $('#output').html('<div class="form-group"><p>Download report: <a href="'+response['url']+'">'+response['url']+'</a></p></div>')
                }
                if (response['error']){
                    $("#output").html("<div class='alert alert-danger'>" +
                    response['error'] +"</div>");
                }
                
                console.log("ajax successful");

            },
            cache: false,
            contentType: false,
            processData: false,
            error: function (request, status, error) {
                console.log(request.responseText);
           }
        });
        
    });

    

  });