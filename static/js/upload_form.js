$(document).ready(function () {
    $('[type="checkbox"][name="pivot"]').change(function(){
        if(this.checked){
            $('#pivot-input').fadeIn(this.checked);
            $('#basic-input').fadeOut(this.checked);
        }
        else{
            $('#pivot-input').fadeOut(this.checked);
        }
      
    });
    $('[type="checkbox"][name="basic"]').change(function(){
        if(this.checked){
            $('#basic-input').fadeIn(this.checked);
            $('#pivot-input').fadeOut(this.checked);
        }
        else{
            $('#basic-input').fadeOut(this.checked);
        }
      
    });


  });