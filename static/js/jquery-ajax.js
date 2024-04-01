$(document).ready(function () {

    $(document).on('click', '.ajax-link', function (e) {
        e.preventDefault();
        var cartQtyTemp = $('#ajax-qty');
        var cartQty = parseInt(cartQtyTemp.text() || 0);

        var productIdTag = $(".ajax-add");
        var productId = productIdTag.data('product-id')
        console.log(productId);

        var cartAddUrl = $(this).attr('action');
        console.log(cartAddUrl)

        $.ajax({
            url: cartAddUrl,
            method: 'post',
            data: {
                'product_id': productId,
                'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
                'size': $("[name=size]").val(),
            },
            success: function(response) {

                cartQty++;
                cartQtyTemp.text(cartQty);
            },
            error: function(response) {
                console.log('Error: ', response)
            },
        });
    });
});