$(document).ready(function() {
    var container = $(".cont1");
    container.addClass("container")

    var row = $("<div>").addClass("row").text("Popular Items: ");
    container.append(row);


    var list = $("<ul>").addClass("popular-items");

    container.append(list);

    console.log(restaurant["Popular Menu Items"])

    $.each(restaurant["Popular Menu Items"], function(index, item) {
        var listItem = $("<li>").text(item);

        list.append(listItem);
    });
});

$(document).ready(function() {
    var container = $(".cont2");
    container.addClass("container")

    var row = $("<div>").addClass("row").text("Restaurants Similair in Price: ");
    container.append(row);


    var list = $("<ul>").addClass("rests");

    container.append(list);

    console.log(restaurant["Similair Restaurants"])
    if(restaurant["Similair Restaurants"].length > 0){
        $.each(restaurant["Similair Restaurants"], function(index, item) {

            var listItem = $("<li>").text(restaurants[item]["Name"]).addClass("restaurant-item");
            listItem.on('click', function() {
                window.location.href = '/view/' + item;
            });
            list.append(listItem);
        });
    }
    else{
        var noRestMessage = $("<li>").text("No restaurants found");
        list.append(noRestMessage);
    }
});

$(document).ready(function() {
    function displayStars(rating) {
        let stars = "";
        for (let i = 1; i <= 5; i++) {
            if (i <= rating) {
                stars += "★"; 
            } else {
                stars += "☆"; 
            }
        }
        return stars;
    }

    $("#star-rating").html(displayStars(restaurant["Rating"]));
});

$(document).ready(function() {
    $('.address').click(function() {
        window.location.href = "/get-directions/" + restaurant["Id"];
    });
});



