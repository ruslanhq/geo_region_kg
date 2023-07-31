from rest_framework import serializers
from apps.geo_data.models import Contour


class ContourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contour
        fields = ('id', 'geometry')
