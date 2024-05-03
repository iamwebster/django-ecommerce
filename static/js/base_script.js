$(document).ready(function () {

    $('.nav__wrap li').hover(
        function () {
            $('ul', this).stop().slideDown(100);

        }, 
        function () {
            $('ul', this).stop().slideUp(100);			
        }
    );
})