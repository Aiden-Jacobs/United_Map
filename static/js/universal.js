var map = L.map('map').fitWorld().setView([39.8283, -98.5795], 4);//.flyTo([39.8283, -98.5795], 4)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

console.log("test of js file");


/* Latitude/longitude spherical geodesy tools                         (c) Chris Veness 2002-2021  */
/*                                                                                   MIT Licence  */
function midPoint(lat1, lon1, lat2, lon2, depth, points){
    var out  = []
    const φ1 = lat1 * Math.PI/180, φ2 = lat2 * Math.PI/180 // latitude in rads
    const λ2 = lon2 * Math.PI/180, λ1 = lon1 * Math.PI/180 // longitude in rads
    const Bx = Math.cos(φ2) * Math.cos(λ2-λ1);
    const By = Math.cos(φ2) * Math.sin(λ2-λ1);
    const φ3 = (180*(Math.atan2(Math.sin(φ1) + Math.sin(φ2),
                          Math.sqrt( (Math.cos(φ1)+Bx)*(Math.cos(φ1)+Bx) + By*By ) )))/Math.PI;
    const λ3 = (180*(λ1 + Math.atan2(By, Math.cos(φ1) + Bx)))/Math.PI;
    depth -= 1;
    if (depth > 0) {
        
        var result2 = midPoint(lat1, lon1,φ3, λ3, depth, points)
        
        result2.forEach(element => {
            out.push(element)
        });
        out.push([φ3, λ3])
        var result = midPoint(φ3, λ3,lat2, lon2, depth, points)
        result.forEach(element => {
            out.push(element)
        });
        
        return (out);
    }else{

        return ([]);
    }
    
}

function addCurve(latlong,smoothness)//smoothness is exponential 
{
    var temp = latlong.pop()
    var mid = midPoint(latlong[0][0],latlong[0][1],temp[0],temp[1],smoothness,[])
    mid.forEach(element => {
        latlong.push(element)
    });
    latlong.push(temp)
}

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

    addCurve(latlong,5)

    //console.log(midPoint(latlong[0][0],latlong[0][1],latlong[1][0],latlong[1][1],5,[]))
    var path = new L.polyline(latlong, {
    color: c,
    weight: 2.5,
    opacity: .7,
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
