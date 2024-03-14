$(document).ready(function() {
    $("#search_box").submit(function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        var searchText = $.trim($("#validationInput").val());

        if (searchText !== "") {
            window.location.href = "/search_results/" + encodeURIComponent(searchText);
        } else {
            $("#validationInput").val("");
            $("#validationInput").focus();
        }
    });
});