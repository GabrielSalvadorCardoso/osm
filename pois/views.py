from django.http import HttpResponse

from hyper_resource.resources.AbstractResource import AbstractResource, JSON_CONTENT_TYPE, CONTENT_TYPE_JSONLD
from hyper_resource.resources.FeatureCollectionResource import FeatureCollectionResource
from hyper_resource.resources.FeatureResource import FeatureResource
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import *
from django.shortcuts import get_object_or_404

class APIRoot(AbstractResource):

    def add_entry_point_link_header(self, request, response):
        entry_point_uri = request.build_absolute_uri()[:-1]
        link_content = '<' + entry_point_uri + '>; rel="https://schema.org/EntryPoint", '
        link_content += '<' + entry_point_uri + '.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
        response["Link"] = link_content

    def get_entry_point_data(self, request, *args, **kwargs):
        return {
            "points-of-interest": reverse("pois:Pois_list", args=args, kwargs=kwargs, request=request),
            "bicycle-rental": reverse("pois:BicycleRental_list", args=args, kwargs=kwargs, request=request),
            "monument": reverse("pois:Monument_list", args=args, kwargs=kwargs, request=request),
            "park": reverse("pois:Park_list", args=args, kwargs=kwargs, request=request),
            "viewpoint": reverse("pois:Viewpoint_list", args=args, kwargs=kwargs, request=request),
            "road": reverse("pois:Road_list", args=args, kwargs=kwargs, request=request),
        }

    def get(self, request, *args, **kwargs):
        data = self.get_entry_point_data(request, *args, **kwargs)
        response = Response(data, status=status.HTTP_200_OK, content_type=JSON_CONTENT_TYPE)
        self.add_entry_point_link_header(request, response)
        return response

    # todo: maybe this content make more sanse in contexts.py
    def options(self, request, *args, **kwargs):
        entry_point_keys = self.get_entry_point_data(request, *args, **kwargs).keys()
        context = {"@context": {"hydra": "https://www.w3.org/ns/hydra/core#"}}
        for key in entry_point_keys:
            context["@context"].update({
                key: {
                    "@id": "https://purl.org/geojson/vocab#FeatureCollection",
                    "@type": "@id"
                }
            })

        context["hydra:supportedProperty"] = []

        for key in entry_point_keys:
            context["hydra:supportedProperty"].append({
                "hydra:property": key,
                "hydra:writable": False,
                "hydra:readable": True,
                "hydra:required": False
            })

        response = Response(context, status=status.HTTP_200_OK, content_type=CONTENT_TYPE_JSONLD)
        self.add_entry_point_link_header(request, response)
        return response

class PoisList(FeatureCollectionResource):
    serializer_class = PoisSerializer

class PoisDetail(FeatureResource):
    serializer_class = PoisSerializer

#http://localhost:8060/api/osm/bicycle-rental/within/http://localhost:8000/api/restful-ide/bcim/unidades-federativas/RJ
class BicycleRentalList(FeatureCollectionResource):
    serializer_class = BicycleRentalSerializer

class BicycleRentalDetail(FeatureResource):
    serializer_class = BicycleRentalSerializer

    def get_object(self, **kwargs):
        query_dict = self.get_object_query_dict(**kwargs)
        try:
            query_dict = {self.serializer_class.Meta.id_field: query_dict["pk"]}
        except KeyError:
            pass
        return get_object_or_404(self.serializer_class.Meta.model, **query_dict)

class MonumentList(FeatureCollectionResource):
    serializer_class = MonumentSerializer

class MonumentDetail(FeatureResource):
    serializer_class = MonumentSerializer

class ParkList(FeatureCollectionResource):
    serializer_class = ParkSerializer

class ParkDetail(FeatureResource):
    serializer_class = ParkSerializer

class ViewpointList(FeatureCollectionResource):
    serializer_class = ViewpointSerializer

class ViewpointDetail(FeatureResource):
    serializer_class = ViewpointSerializer

class RoadList(FeatureCollectionResource):
    serializer_class = RoadSerializer

class RoadDetail(FeatureResource):
    serializer_class = RoadSerializer

class Style(AbstractResource):

    def get(self, request, *args, **kwargs):
        with open(kwargs["icon_name"], "r") as file:
            return HttpResponse(file.read(), content_type="image/svg+xml", status=200)