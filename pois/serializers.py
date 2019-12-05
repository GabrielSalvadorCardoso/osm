from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *

class PoisSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Pois
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'fclass', 'name']

class RoadSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Road
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ["gid", "fclass", "name", "ref", "oneway", "maxspeed", "layer", "bridge", "tunnel"]

class BicycleRentalSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BicycleRental
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'name']

class MonumentSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Monument
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'name']

class ParkSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Park
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'name']

class ViewpointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Viewpoint
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'name']