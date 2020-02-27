(function(){
    var pivot = document.getElementById("id_pivot");
    //var basic = document.getElementById("id_basic");
    var pivot_input = document.getElementById("pivot__input");
    var basic_input = document.getElementById("basic__input");
    pivot_input.style.display = "none";
    pivot.onclick=function(){
        if(pivot_input.style.display=="none"){
            pivot_input.style.display="block";
            basic_input.style.display="none";
        }
        else{
            pivot_input.style.display="none";
            basic_input.style.display="block";
        }
    }

    basic.onclick=function(){
        if(basic_input.style.display=="none"){
            basic_input.style.display="block";
            pivot_input.style.display="none";
        }
        else{
            basic_input.style.display="none";
            pivot_input.style.display="block";
        }
    }

})();


