let map;

async function initMap(latitude, longitude) {
  const position = { lat: latitude, lng: longitude };

  // Assuming google.maps is already available
  // Request needed libraries.
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  // Use jQuery to select the DOM element
  map = new Map($("#map")[0], {
    zoom: 15,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  // The marker, positioned at Uluru
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "Uluru",
  });
}

$(document).ready(function() {
  initMap();
});



function getCoordinatesFromAddress(address) {
    return new Promise((resolve, reject) => {
        var api_key = API_Key_Here;
        var url = `https://maps.googleapis.com/maps/api/geocode/json?address=${encodeURIComponent(address)}&key=${api_key}`;

        $.ajax({
            url: url,
            type: 'GET',
            success: function(data) {
                if (data['status'] === 'OK') {
                    var latitude = data['results'][0]['geometry']['location']['lat'];
                    var longitude = data['results'][0]['geometry']['location']['lng'];
                    resolve({latitude, longitude});
                } else {
                    reject("Error: " + data['status']);
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                reject("Request Failed: " + textStatus);
            }
        });
    });
}
function logCoordinatesForAddress(address) {
    getCoordinatesFromAddress(address)
        .then(coordinates => {
            initMap(coordinates.latitude, coordinates.longitude);

        })
        .catch(error => {
            console.error(error);
        });
}
$(document).ready(function() {
    logCoordinatesForAddress(restaurant["Address"]);
});



function createMapWithMarker(latitude, longitude, title = "Marker Title") {
    var mapElement = `<gmp-map center="${latitude}, ${longitude}" zoom="14" map-id="DEMO_MAP_ID">
        <gmp-advanced-marker position="${latitude}, ${longitude}" title="${title}"></gmp-advanced-marker>
    </gmp-map>`;

    $('#mapContainer').empty().append(mapElement);
}

