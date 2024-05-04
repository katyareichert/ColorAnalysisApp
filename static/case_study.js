$(document).ready(function() {
    console.log(slide);
    console.log(typeof slide);
    console.log(slide === '1');

    if (slide === '1') {
        $('#fade_image').fadeOut(2000);
        $('#square').animate({
            left: '+=356px'
        }, 2000);
    }
})