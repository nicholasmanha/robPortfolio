$(function () {
    $(window).on('scroll', function () {
        if ( $(window).scrollTop() > 10 ) {
            $('.navbar').addClass('active');
            $('.logo').addClass('active');
            $('.logo2').addClass('active');
        } else {
            $('.logo2').removeClass('active');
            $('.navbar').removeClass('active');
            $('.logo').removeClass('active');
        }
    });
});