from django.contrib.gis.db import models


class Region(models.Model):
    title = models.CharField(max_length=255)
    geometry = models.PolygonField()

    def __str__(self):
        return self.title


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    geometry = models.PolygonField()

    def __str__(self):
        return self.title


class Canton(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    geometry = models.PolygonField()

    def __str__(self):
        return self.title


class Contour(models.Model):
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE)
    geometry = models.PolygonField()

