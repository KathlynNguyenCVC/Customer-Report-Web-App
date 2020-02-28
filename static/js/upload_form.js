$(document).ready(function () {
    $('#id_permission_0').attr("disabled",true);

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


  });