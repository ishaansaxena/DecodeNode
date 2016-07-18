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
        var image = "linear-gradient(rgba($accent, 0.85), rgba($accent, 0.85)), url('" + $(this).attr('data') + "')";
        $(this).css({
            'background': image
        });
        console.log(image);
    });
    background: linear-gradient(rgba($accent, 0.85), rgba($accent, 0.85));
});