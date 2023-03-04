function myFunction(berger) {
    berger.classList.toggle("onoff");
}

function toogleSlideMenu(berger) {
    if (berger.classList.contains('onoff')) {
        document.getElementById("burger-icon").classList.remove('fa-bars-staggered');
        document.getElementById("burger-icon").classList.add('fa-times');
        document.getElementById("responsive-nav-overlay").style.width = "250px";  

    } else {
        document.getElementById("burger-icon").classList.remove('fa-times');
        document.getElementById("burger-icon").classList.add('fa-bars-staggered');
        document.getElementById("responsive-nav-overlay").style.width = "0";
       
    }
}