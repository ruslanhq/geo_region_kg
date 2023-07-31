from django.urls import path
from apps.geo_data.views import ContourListView

urlpatterns = [
    path('contours/', ContourListView.as_view(), name='contour-list'),
]
