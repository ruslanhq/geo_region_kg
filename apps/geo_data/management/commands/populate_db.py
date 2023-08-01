from django.contrib.gis.geos import Polygon
from django.core.management.base import BaseCommand

from apps.geo_data.models import Region, District, Canton, Contour


def populate_database():
    region = Region.objects.create(
        title='Чуйская область',
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )

    # Создание районов
    district1 = District.objects.create(
        region=region,
        title='Панфиловский район',
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )
    district2 = District.objects.create(
        region=region,
        title='Московский район',
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )
    district3 = District.objects.create(
        region=region,
        title='Сокулукский район',
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )

    # Создание айыльных округов
    canton1 = Canton.objects.create(
        district=district1,
        title='Ак-Бешимский айыльный округ',
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )
    canton2 = Canton.objects.create(
        district=district1,
        title='Кошойский айыльный округ',
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )
    canton3 = Canton.objects.create(
        district=district2,
        title='Беловодский айыльный округ',
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )
    canton4 = Canton.objects.create(
        district=district2,
        title='Лебединовский айыльный округ',
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )

    # Создаем контуры
    contour1 = Contour.objects.create(
        canton=canton1,
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )
    contour1 = Contour.objects.create(
        canton=canton1,
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )
    contour1 = Contour.objects.create(
        canton=canton2,
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )
    contour1 = Contour.objects.create(
        canton=canton2,
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )
    contour1 = Contour.objects.create(
        canton=canton3,
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )
    contour1 = Contour.objects.create(
        canton=canton3,
        geometry=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )


class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        populate_database()
