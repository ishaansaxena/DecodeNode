$(document).ready(function(){
    $('.trigger').click(function(){
        $('#menu').toggleClass('visible');
        $('#container').toggleClass('hidden');
    });
    $('#container').click(function(){
        if ($('#menu').hasClass('visible')){
            $('#menu').removeClass('visible');
            $('#container').removeClass('hidden');
        }
    });
    $('.menu-header').each(function(){
        console.log($(this).attr('data'));
    });
});