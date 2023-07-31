import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.gis.geos import Polygon
from apps.geo_data.models import Region, District, Canton


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


if __name__ == '__main__':
    populate_database()
