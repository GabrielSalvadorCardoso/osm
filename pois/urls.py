from django.urls import path, re_path
from .views import *

app_name = "pois"
urlpatterns = [
    path('', APIRoot.as_view(), name="root"),

    re_path('^pois/(?P<pk>[0-9]+)/(?P<operation_or_attributes>.+)/?$', PoisDetail.as_view(), name='Pois_detail_operation_or_attributes'),
    re_path('^pois/(?P<sigla>[A-Za-z]{2})/(?P<operation_or_attributes>.+)/?$', PoisDetail.as_view(), name='Pois_bysigla_operation_or_attributes'),
    path('pois/<int:pk>.<str:extension>', PoisDetail.as_view(), name='Pois_detail_extension'),
    re_path('^pois/(?P<sigla>[A-Za-z]{2})(?P<extension>\..+)/?$', PoisDetail.as_view(), name='Pois_bysigla_extension'),
    path('pois/<int:pk>', PoisDetail.as_view(), name='Pois_detail'),
    re_path('^pois/(?P<sigla>[A-Za-z]{2})/?$', PoisDetail.as_view(), name='Pois_bysigla_detail'),
    path('pois/<path:operation_or_attributes>/', PoisList.as_view(), name='Pois_list_operation_or_attributes'),
    path('pois.<str:extension>', PoisList.as_view(), name='Pois_list_extension'),
    path('pois', PoisList.as_view(), name='Pois_list'),

    re_path('^roads(?P<pk>[0-9]+)/(?P<operation_or_attributes>.+)/?$', RoadDetail.as_view(), name='Road_detail_operation_or_attributes'),
    re_path('^road/(?P<sigla>[A-Za-z]{2})/(?P<operation_or_attributes>.+)/?$', RoadDetail.as_view(), name='Road_bysigla_operation_or_attributes'),
    path('road/<int:pk>.<str:extension>', RoadDetail.as_view(), name='Road_detail_extension'),
    re_path('^roads/(?P<sigla>[A-Za-z]{2})(?P<extension>\..+)/?$', RoadDetail.as_view(), name='Road_bysigla_extension'),
    path('road/<int:pk>', RoadDetail.as_view(), name='Road_detail'),
    re_path('^road/(?P<sigla>[A-Za-z]{2})/?$', RoadDetail.as_view(), name='Road_bysigla_detail'),
    path('road/<path:operation_or_attributes>/', RoadList.as_view(), name='Road_list_operation_or_attributes'),
    path('road.<str:extension>', RoadList.as_view(), name='Road_list_extension'),
    path('road', RoadList.as_view(), name='Road_list'),

    re_path('^bicycle-rental/(?P<pk>[0-9]+)/(?P<operation_or_attributes>.+)/?$', BicycleRentalDetail.as_view(), name='BicycleRental_detail_operation_or_attributes'),
    re_path('^bicycle-rental/(?P<sigla>[A-Za-z]{2})/(?P<operation_or_attributes>.+)/?$', BicycleRentalDetail.as_view(), name='BicycleRental_bysigla_operation_or_attributes'),
    path('bicycle-rental/<int:pk>.<str:extension>', BicycleRentalDetail.as_view(), name='BicycleRental_detail_extension'),
    re_path('^bicycle-rental/(?P<sigla>[A-Za-z]{2})(?P<extension>\..+)/?$', BicycleRentalDetail.as_view(), name='BicycleRental_bysigla_extension'),
    path('bicycle-rental/<int:pk>', BicycleRentalDetail.as_view(), name='BicycleRental_detail'),
    re_path('^bicycle-rental/(?P<sigla>[A-Za-z]{2})/?$', BicycleRentalDetail.as_view(), name='BicycleRental_bysigla_detail'),
    path('bicycle-rental/<path:operation_or_attributes>/', BicycleRentalList.as_view(), name='BicycleRental_list_operation_or_attributes'),
    path('bicycle-rental.<str:extension>', BicycleRentalList.as_view(), name='BicycleRental_list_extension'),
    path('bicycle-rental', BicycleRentalList.as_view(), name='BicycleRental_list'),

    re_path('^monument/(?P<pk>[0-9]+)/(?P<operation_or_attributes>.+)/?$', MonumentDetail.as_view(), name='Monument_detail_operation_or_attributes'),
    re_path('^monument/(?P<sigla>[A-Za-z]{2})/(?P<operation_or_attributes>.+)/?$', MonumentDetail.as_view(), name='Monument_bysigla_operation_or_attributes'),
    path('monument/<int:pk>.<str:extension>', MonumentDetail.as_view(), name='Monument_detail_extension'),
    re_path('^monument/(?P<sigla>[A-Za-z]{2})(?P<extension>\..+)/?$', MonumentDetail.as_view(), name='Monument_bysigla_extension'),
    path('monument/<int:pk>', MonumentDetail.as_view(), name='Monument_detail'),
    re_path('^monument/(?P<sigla>[A-Za-z]{2})/?$', MonumentDetail.as_view(), name='Monument_bysigla_detail'),
    path('monument/<path:operation_or_attributes>/', MonumentList.as_view(), name='Monument_list_operation_or_attributes'),
    path('monument.<str:extension>', MonumentList.as_view(), name='Monument_list_extension'),
    path('monument', MonumentList.as_view(), name='Monument_list'),

    re_path('^park/(?P<pk>[0-9]+)/(?P<operation_or_attributes>.+)/?$', MonumentDetail.as_view(), name='Park_detail_operation_or_attributes'),
    re_path('^park/(?P<sigla>[A-Za-z]{2})/(?P<operation_or_attributes>.+)/?$', MonumentDetail.as_view(), name='Park_bysigla_operation_or_attributes'),
    path('park/<int:pk>.<str:extension>', MonumentDetail.as_view(), name='Park_detail_extension'),
    re_path('^park/(?P<sigla>[A-Za-z]{2})(?P<extension>\..+)/?$', MonumentDetail.as_view(), name='Park_bysigla_extension'),
    path('park/<int:pk>', MonumentDetail.as_view(), name='Park_detail'),
    re_path('^park/(?P<sigla>[A-Za-z]{2})/?$', MonumentDetail.as_view(), name='Park_bysigla_detail'),
    path('park/<path:operation_or_attributes>/', MonumentList.as_view(), name='Park_list_operation_or_attributes'),
    path('park.<str:extension>', MonumentList.as_view(), name='Park_list_extension'),
    path('park', MonumentList.as_view(), name='Park_list'),

    re_path('^viewpoint/(?P<pk>[0-9]+)/(?P<operation_or_attributes>.+)/?$', ViewpointDetail.as_view(), name='Viewpoint_detail_operation_or_attributes'),
    re_path('^viewpoint/(?P<sigla>[A-Za-z]{2})/(?P<operation_or_attributes>.+)/?$', ViewpointDetail.as_view(), name='Viewpoint_bysigla_operation_or_attributes'),
    path('viewpoint/<int:pk>.<str:extension>', ViewpointDetail.as_view(), name='Viewpoint_detail_extension'),
    re_path('^viewpoint/(?P<sigla>[A-Za-z]{2})(?P<extension>\..+)/?$', ViewpointDetail.as_view(), name='Viewpoint_bysigla_extension'),
    path('viewpoint/<int:pk>', ViewpointDetail.as_view(), name='Viewpoint_detail'),
    re_path('^viewpoint/(?P<sigla>[A-Za-z]{2})/?$', ViewpointDetail.as_view(), name='Viewpoint_bysigla_detail'),
    path('viewpoint/<path:operation_or_attributes>/', ViewpointList.as_view(), name='Viewpoint_list_operation_or_attributes'),
    path('viewpoint.<str:extension>', ViewpointList.as_view(), name='Viewpoint_list_extension'),
    path('viewpoint', ViewpointList.as_view(), name='Viewpoint_list'),

    path('styles/<str:icon_name>', Style.as_view(), name='Style_list'),
]