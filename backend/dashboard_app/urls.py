from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    InsightEntryViewSet,
    FiltersView,
    IntensityByYearView,
    LikelihoodTrendView,
)

router = DefaultRouter()
router.register(r'entries', InsightEntryViewSet, basename='entries')

urlpatterns = [
    path('', include(router.urls)),
    path('filters/', FiltersView.as_view(), name='filters'),
    path('aggregations/intensity-by-year/', IntensityByYearView.as_view(), name='intensity-by-year'),
    path('aggregations/likelihood-trend/', LikelihoodTrendView.as_view(), name='likelihood-trend'),
]
