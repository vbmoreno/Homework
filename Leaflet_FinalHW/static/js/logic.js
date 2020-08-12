// Creating map object
// Store API query variables
var baseURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson";

// Creating map object
var mymap = L.map("map", {
  center: [40.7, -73.95],
  zoom: 11
});

var mymap = L.map('map-id').setView([51.505, -0.09], 13);


});


L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'vbmoreno',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'ckdorpt3h0vyo26mrjmfj6e16-6ec3r'
}).addTo(mymap);

});

var map = new L.map("map", {
    center: [51.505, -0.09],
    zoom: 3,
    minZoom: 2,
    maxZoom: 18
    
});

var marker = L.marker[51.505, -0.09].addTo(mymap);
});

var circle = L.circle([51.505, -0.09])
	color; 'blue'
	fillColor: '#f03',
	fillOpacity: 0.5,
	radius: 500
}).addTo(mymap);
});


marker.bindPopup("<b>Hello Friend!</b><br>Earthquakes are Real.").openPopup();
circle.bindPopup("This is important.");
polygon.bindPopup("This is important.");

});
