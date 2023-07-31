from django.contrib import admin
from apps.geo_data.models import Region, District, Canton, Contour


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('title', 'region')
    list_filter = ('region',)
    search_fields = ('title',)


@admin.register(Canton)
class CantonAdmin(admin.ModelAdmin):
    list_display = ('title', 'district')
    list_filter = ('district__region', 'district')
    search_fields = ('title',)


@admin.register(Contour)
class ContourAdmin(admin.ModelAdmin):
    list_display = ('id', 'canton')
    list_filter = ('canton__district__region', 'canton__district', 'canton')
