wget -O "buildings_way.geojson" "https://overpass-api.de/api/interpreter?data=way[building](37.451967,14.658508,38.021050,15.298462);(._;>;);out;"
wget -O "buildings_rel.geojson" "https://overpass-api.de/api/interpreter?data=rel[building](37.451967,14.658508,38.021050,15.298462);(._;>;);out;"
#wget -O "streets.geojson" "https://overpass-api.de/api/interpreter?data=way[highway](37.451967,14.658508,38.021050,15.298462);(._;>;);out;"

#python ./etna/vulnerability.py