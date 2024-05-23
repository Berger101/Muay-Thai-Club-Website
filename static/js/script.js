// Google maps
function initMap() {
  // The location of the initial marker
  const location = { lat: -25.344, lng: 131.036 }; // Example coordinates (Uluru, Australia)
  // The map, centered at the location
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: location,
  });
  // The marker, positioned at the location
  const marker = new google.maps.Marker({
    position: location,
    map: map,
  });
}