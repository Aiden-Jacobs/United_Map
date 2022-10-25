var map = L.map('map').fitWorld().setView([39.8283, -98.5795], 4);//.flyTo([39.8283, -98.5795], 4)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

console.log("test of js file");

function addPath(latlong,steps) {
    //console.log(steps)
    var c = '#0000FF';
    if(steps == 1){
        c = '#006600';
        
    }
    if (steps == 2) {
        c ='#206620'
    }
    if (steps == 3) {
        c = '#666600'
    }
    if (steps == 4) {
        c = '#FF0000'
    }
    var path = new L.polyline(latlong, {
    color: c,
    weight: 10/steps,
    opacity: 0.1,
    smoothFactor: 1
    }).addTo(map);
    //map.addLayer(path);
  }

  function addPoint(latlong,name) {
    //console.log(name)
    var path = new L.polyline(latlong, {
    color: '#1111bb',
    weight: 7,
    opacity: 1,
    smoothFactor: 1
    }).addTo(map).bindPopup(name);
    //map.addLayer(path);
  }

var latlong = [
    [37.6213, -122.3790],
    [39.8561, -104.6737],
    [29.9911, -90.2592]
    ];

//addPath(latlong)
