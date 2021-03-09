function expandnav() {
    var change = document.getElementById("change");
    if (change.style.height === "200px"){
        change.style.height = "0";
    }
    else{
        change.style.height = "200px";
    }
}
$(window).on('resize', function(event){
    var windowSize = $(window).width(); 
    if(windowSize < 640){
        $("#change").css('display', 'block');
        $("#change").css('height', '0px');
    } else {
        $("#change").css('display', 'flex');
    }
});