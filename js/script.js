function expandnav() {
    var change = document.getElementById("change");
    if (change.style.display === "block"){
        change.style.display = "none";
    }
    else{
        change.style.display = "block";
    }
}
$(window).on('resize', function(event){
    var windowSize = $(window).width(); 
    if(windowSize < 613){
        $("#change").css('display', 'none');
    } else {
        $("#change").css('display', 'flex');
    }
});