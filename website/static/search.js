$(document).ready(function() {
    function highlightMatchingText(input, text) {
        var index = text.toLowerCase().indexOf(input.toLowerCase());
        if (index !== -1) {
            return text.substring(0, index) + "<strong>" + text.substring(index, index + input.length) + "</strong>" + text.substring(index + input.length);
        } else {
            return text;
        }
    }

    $("#search-input").text("Showing results for \"" + input + "\"");

    if(results.length > 0 || blurbs.length > 0 || price.length > 0){
        var total = results.length + blurbs.length + price.length
        var num_res = $("<div>").addClass("container").html("<div class='row'>" + total + " results found</div>");
        $("#total-results").append(num_res);


        if (results.length > 0) {
            var resultsContainer = $("<div>").addClass("container");
            $.each(results, function(index, result) {
                var highlightedName = highlightMatchingText(input, result["Name"]);
                var resultRow = $("<div>").addClass("restaurant-link").html(highlightedName);
                resultRow.click(function() {
                    window.location.href = "/view/" + result["Id"];
                });
                resultsContainer.append(resultRow);
            });
            $("#results-container").append(resultsContainer);
        }
        
        if (blurbs.length > 0) {
            var blurbsCont = $("<div>").addClass("container");
            $.each(blurbs, function(index, blurbs) {
                var highlightedBlurb = highlightMatchingText(input, blurbs["Restaurant Blurb"]);
                var resultRow = $("<div>").addClass("restaurant-blurb blurb-link").html(highlightedBlurb);
                resultRow.click(function() {
                    window.location.href = "/view/" + blurbs["Id"];
                });
                blurbsCont.append(resultRow);

            });
            $("#results-container").append(blurbsCont);
        }
        if (price.length > 0) {
            var priceCont = $("<div>").addClass("container");
            $.each(price, function(index, price) {
                var highlightedBlurb = highlightMatchingText(input, price["Price Level"]);
                var resultText = price["Name"] + " is " + highlightedBlurb;

                var resultRow = $("<div>").addClass("restaurant-blurb blurb-link").html(resultText);
                
                resultRow.click(function() {
                    window.location.href = "/view/" + price["Id"];
                });
                priceCont.append(resultRow);

            });
            $("#results-container").append(priceCont);
        }





    } else {
        var noResults = $("<div>").addClass("container").html("<div class='row'>No results found</div>");
        $("#no-results").append(noResults);
    }
});






