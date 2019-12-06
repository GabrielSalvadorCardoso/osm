# osm
osm uses python3 and pip

## intall project python dependencies
pip install -r requirements.txt

## osm uses mapnik, to install it
https://github.com/mapnik/mapnik/wiki/UbuntuInstallation

## in the case of errors involving the C++ compiler
https://github.com/mapnik/mapnik/issues/3769

## install mapnik python bidings
pip3 install mapnik

## if the previous command doesn't work
https://github.com/mapnik/python-mapnik

osm uses PostgreSQL with spatial extansion PostGIS. Feel free to use whatever database with spatial extansion you want

## osm spatial data (Brazil - .shp.zip)
http://download.geofabrik.de/south-america.html

## using shp2pgsql to transfer shapefiles to postgres/postgis
https://www.bostongis.com/pgsql2shp_shp2pgsql_quickguide.bqg
