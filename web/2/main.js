$(document).ready(function(){
    $('.fa-bars').click(function(){
        $(this).toggleClass('fa-times');
        $('.navbar').toggleClass('nav-toggle');
    });
    $(window).on('load scroll',function(){
        $('.fa-bars').removeClass('fa-times');
        $('.navbar').removeClass('nav-toggle');
        if($(window).scrollTop() > 30){
            $('.header__section').css({'background':'#6c5ce7','box-shadow':'0 .2rem .5rem rgba(0,0,0,.4)'});
        }else{
            $('.header__section').css({'background':'none','box-shadow':'none'});

        }
    });

    $('.accordion-header').click(function(){
        $('.accordion .accordion-body').slideUp(500);
        $(this).next('.accordion-body').slideDown(500);
        $('.accordion .accordion-header span').text('+');
        $(this).children('span').text('-');
    });
});        