# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models
from hyper_resource.models import FeatureModel

class Pois(FeatureModel):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pois'

class Road(FeatureModel):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    oneway = models.CharField(max_length=1, blank=True, null=True)
    maxspeed = models.SmallIntegerField(blank=True, null=True)
    layer = models.FloatField(blank=True, null=True)
    bridge = models.CharField(max_length=1, blank=True, null=True)
    tunnel = models.CharField(max_length=1, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roads'

class BicycleRental(FeatureModel):
    #gid = models.IntegerField(blank=True, null=True)
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'bicycle_rental'


class Monument(FeatureModel):
    # gid = models.IntegerField(blank=True, null=True)
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'monument'


class Park(FeatureModel):
    # gid = models.IntegerField(blank=True, null=True)
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'park'


class Viewpoint(FeatureModel):
    # gid = models.IntegerField(blank=True, null=True)
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'viewpoint'