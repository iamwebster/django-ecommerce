$(document).ready(function () {

    $(document).on('click', '.ajax-add', function (e) {
        e.preventDefault();

        var cartQtyTemp = $('#ajax-qty');
        var cartQty = parseInt(cartQtyTemp.text() || 0);

        var productId = $(this).data('product-id');

        var cartAddUrl = $(this).attr('href');

        $.ajax({
            url: cartAddUrl,
            method: 'post',
            data: {
                'product_id': productId,
                'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function(response) {
                console.log(response.message);

                cartQty++;
                cartQtyTemp.text(cartQty);
            },
            error: function(response) {
                console.log('Error: ', response)
            },
        });
    });

});