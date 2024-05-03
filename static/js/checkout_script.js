$(document).ready(function () {
    $('.checkout__open').click(function() {
        $('.checkout__fade').fadeIn();
        return false;
    });	
    
    $('.checkout__close').click(function() {
        $(this).parents('.checkout__fade').fadeOut();
        return false;
    });		

    $(document).keydown(function(e) {
        if (e.keyCode === 27) {
            e.stopPropagation();
            $('.checkout__fade').fadeOut();
        }
    });
    
    $('.checkout__fade').click(function(e) {
        if ($(e.target).closest('.checkout__wrap').length == 0) {
            $(this).fadeOut();					
        }
    });	


    $("#deliveryAddressField").hide(); 

    
    $("input[name='need_delivery']").change(function() { 
        var selectedValue = $(this).val(); 
        if (selectedValue === "1") { 
            $("#deliveryAddressField").show(); 
            $("#id_delivery_address").prop('required', true); 
        } else {
            $("#deliveryAddressField").hide(); 
            $("#id_delivery_address").prop('required', false);
        }
    });
});