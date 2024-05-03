$(document).ready(function () {

    $(document).keypress(function(event){
        if (event.which == '13') {
            event.preventDefault();
            $('.sidebar__button').trigger('click');
        }
    });
})