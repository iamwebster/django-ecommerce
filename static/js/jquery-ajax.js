$(document).ready(function () {

    $(document).on('click', '.ajax-add', function (e) {
        e.preventDefault();
        var cartQtyTemp = $('#ajax-qty');
        var cartQty = parseInt(cartQtyTemp.text() || 0);

        var productId = $(this).data('product-id')
        var cartAddUrl = $(this).data('link');

        $.ajax({
            url: cartAddUrl,
            method: 'post',
            data: {
                'product_id': productId,
                'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
                'size': $("[name=size]").val(),
            },
            success: function (response) {

                cartQty++;
                cartQtyTemp.text(cartQty);
            },
            error: function (response) {
                console.log('Error: ', response)
            },
        });
    });

    $(document).on('click', '.ajax-remove', function (e) {
        e.preventDefault();
        var cartQtyTemp = $('#ajax-qty');
        var cartQty = parseInt(cartQtyTemp.text() || 0);

        var cartId = $(this).data('cart-id');
        var cartRemoveUrl = $(this).attr('href');

        $.ajax({
            url: cartRemoveUrl,
            method: 'post',
            data: {
                'cart_id': cartId,
                'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (response) {

                $('.cart__item__wrap[data-cart-id="' + cartId + '"]').remove();
                var newTotalPrice = parseFloat($('.cart__result__item__total_grand').text().replace('$', '')) - response.cart_price;
                $('.cart__result__item__total_grand').text('$' + newTotalPrice.toFixed(2));
                var cartItems = $('#cart-items');
                
                cartQty -= response.quantity_deleted;
                cartItems.text(cartQty);
                cartQtyTemp.text(cartQty);

            },
            error: function (response) {
                console.log('Error: ', response)
            },
        });
    });


    $(document).on('click', '.decrement', function () {
        var cartId = $(this).data('cart-id');
        var cartChangeUrl = $(this).data('cart-change-url');

        var $input = $(this).closest('.cart__item__qty__wrap').find('.cart-item-qty');
        var currentValue = parseInt($input.text());

        var price = $(this).closest('.cart__item__wrap').find('.cart__item__total-price')

        if (currentValue > 1) {
            $input.text(currentValue - 1);
            updateCart(cartId, currentValue - 1, -1, cartChangeUrl, price);
        }
    });
    
    $(document).on("click", ".increment", function () {
        var cartId = $(this).data('cart-id');
        var cartChangeUrl = $(this).data('cart-change-url');

        var $input = $(this).closest('.cart__item__qty__wrap').find('.cart-item-qty');
        var currentValue = parseInt($input.text());

        var price = $(this).closest('.cart__item__wrap').find('.cart__item__total-price')

        $input.text(currentValue + 1);
        updateCart(cartId, currentValue + 1, 1, cartChangeUrl, price);

    });

    function updateCart(cartID, quantity, change, url, price) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },

            success: function (response) {
                price.text('$' + response.cart_price)

                var goodsInCartCountTitle = $('#cart-items');
                var cartCountTitle = parseInt(goodsInCartCountTitle.text() || 0);

                var goodsInCartCount = $('#ajax-qty');
                var cartCount = parseInt(goodsInCartCount.text() || 0);

                cartCount += change;
                cartCountTitle += change;
                goodsInCartCount.text(cartCount);
                goodsInCartCountTitle.text(cartCountTitle);

                $('.cart__result__item__total_grand').text('$' + response.total_price).text()

            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    }
});