function loadObservations() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            data.forEach(observation => {
                let shape;
                if (observation.type === "fresh_water") {
                    shape = L.circleMarker([observation.lat, observation.lng], {
                        radius: 10,
                        fillColor: "#00f",
                        color: "#00f",
                        weight: 1,
                        opacity: 1,
                        fillOpacity: 0.5
                    }).addTo(map).bindPopup(`${observation.type}: ${observation.description}`);
                } else if (observation.type === "heat") {
                    shape = L.rectangle([[observation.lat - 0.01, observation.lng - 0.01], 
                                          [observation.lat + 0.01, observation.lng + 0.01]], {
                        color: "#f00",
                        weight: 1,
                        opacity: 1,
                        fillOpacity: 0.5
                    }).addTo(map).bindPopup(`${observation.type}: ${observation.description}`);
                }
                markers.push(shape);
            });
        });
}
