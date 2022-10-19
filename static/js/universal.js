var map = L.map('map').fitWorld().setView([39.8283, -98.5795], 4);//.flyTo([39.8283, -98.5795], 4)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

console.log("test of js file");

function addPath(latlong) {
    var path = new L.polyline(latlong, {
    color: '#006600',
    weight: 3,
    opacity: 0.1,
    smoothFactor: 1
    }).addTo(map);
    //map.addLayer(path);
  }

var latlong = [
    [37.6213, -122.3790],
    [39.8561, -104.6737],
    [29.9911, -90.2592]
    ];

//addPath(latlong)
