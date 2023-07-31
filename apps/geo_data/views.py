from rest_framework import generics
from apps.geo_data.models import Contour
from apps.geo_data.serializers import ContourSerializer


class ContourListView(generics.ListAPIView):
    serializer_class = ContourSerializer

    def get_queryset(self):
        queryset = Contour.objects.all()

        region_id = self.request.query_params.get('region_id')
        if region_id:
            queryset = queryset.filter(canton__district__region_id=region_id)

        district_id = self.request.query_params.get('district_id')
        if district_id:
            queryset = queryset.filter(canton__district_id=district_id)

        canton_id = self.request.query_params.get('canton_id')
        if canton_id:
            queryset = queryset.filter(canton_id=canton_id)

        return queryset
