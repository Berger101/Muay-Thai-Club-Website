// Google maps
function initMap() {
  // The location of the initial marker
  const location = { lat: 55.6050, lng: 13.0038 }; // Example coordinates (Uluru, Australia)
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