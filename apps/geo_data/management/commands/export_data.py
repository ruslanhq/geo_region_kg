import json

from django.core.management import BaseCommand
from django.core.serializers import serialize

from apps.geo_data.models import Region, District, Canton, Contour


def export_data_to_json(filename):
    regions_data = serialize('geojson', Region.objects.all())
    districts_data = serialize('geojson', District.objects.all())
    cantons_data = serialize('geojson', Canton.objects.all())
    contours_data = serialize('geojson', Contour.objects.all())

    data = {
        'regions': json.loads(regions_data),
        'districts': json.loads(districts_data),
        'cantons': json.loads(cantons_data),
        'contours': json.loads(contours_data),
    }

    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


class Command(BaseCommand):
    help = 'Export data from database to json file'

    def handle(self, *args, **kwargs):
        export_data_to_json('geo_data')
