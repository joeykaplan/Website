$(document).ready(function() {
    $('#addRestbutton').click(function() {
        $('#successMessage').hide();
        let Name = $('#rest-name').val();
        let Address = $('#rest-addr').val(); 
        let Price = $('#rest-price').val();
        let ImageLink = $('#rest-pict').val();
        let PopularItem1 = $('#rest-menu1').val();
        let PopularItem2 = $('#rest-menu2').val();
        let Rating = $('#rest-rating').val();
        let Blurb = $('#rest-blurb').val();

        errors = false;

        $('.error-message').remove();

        if (!Blurb) {
            $('#rest-blurb').after('<div class="error-message">Short 75 Char Blurb field is required.</div>');
            $('#rest-blurb').focus();
            errors = true;
        }

        if (!Rating || (isNaN(Rating) || Rating < 1 || Rating > 10)) {
            $('#rest-rating').after('<div class="error-message">Enter a valid rating.</div>');
            $('#rest-rating').focus();
            errors = true;
        }

        if (!PopularItem2) {
            $('#rest-menu2').after('<div class="error-message">Popular item  is required.</div>');
            $('#rest-menu2').focus();
            errors = true;
        }

        if (!PopularItem1) {
            $('#rest-menu1').after('<div class="error-message">Popular item is required.</div>');
            $('#rest-menu1').focus();
            errors = true;
        }

        if (!ImageLink || !isValidUrl(ImageLink)) {
            $('#rest-pict').after('<div class="error-message">Please enter a valid URL for Image Link.</div>');
            $('#rest-pict').focus();
            errors = true;
        }

        if (!Price) {
            $('#rest-price').after('<div class="error-message">Price is required.</div>');
            $('#rest-price').focus();
            errors = true;
        }
        if (!Address) {
            $('#rest-addr').after('<div class="error-message">Address is required.</div>');
            $('#rest-addr').focus();
            errors = true;
        }
        if (!Name) {
            $('#rest-name').after('<div class="error-message">Name is required.</div>');
            $('#rest-name').focus();
            errors = true;
        }


        if(!errors){
            let popularItems = [];
            if (PopularItem1) {
                popularItems.push(PopularItem1);
            }
            if (PopularItem2) {
                popularItems.push(PopularItem2);
            }
        
            let newRest = {
                "Name": Name,
                "Address": Address,
                "Price": Price,
                "ImageLink": ImageLink,
                "PopularItems": popularItems,
                "Rating": Rating,
                "Blurb": Blurb
            };
            addRestaurant(newRest);
            $('#rest-name').val('');
            $('#rest-addr').val('');
            $('#rest-price').val('');
            $('#rest-pict').val('');
            $('#rest-menu1').val('');
            $('#rest-menu2').val('');
            $('#rest-rating').val('');
            $('#rest-blurb').val('');

            $('#rest-name').focus();
        }
    })


    function addRestaurant(newRest) {
        $.ajax({
            url: '/add_rest',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(newRest),
            success: function(response) {
                console.log('Restaurant added successfully:', response);
                showSuccessMessage(response.Id); 
            },
            error: function(xhr, status, error) {
                console.error('Error adding restaurant:', error);
            }
        });
    }
    function showSuccessMessage(restaurantId) {
        $('#successMessage').show();

        $('#viewRestaurantLink').attr('href', '/view/' + restaurantId);
    }



    function isValidUrl(url) {
        let urlRegex = /^(ftp|http|https):\/\/[^ "]+$/;
        return urlRegex.test(url);
    }
})