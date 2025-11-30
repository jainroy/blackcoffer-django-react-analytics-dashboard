from django.db.models import Avg, Count
from django.db.models.functions import Coalesce, ExtractYear
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import InsightEntry
from .serializers import InsightEntrySerializer
from .filters import InsightEntryFilter


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class InsightEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InsightEntry.objects.all().order_by('-id')
    serializer_class = InsightEntrySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = InsightEntryFilter
    search_fields = ['title', 'insight', 'topic', 'sector']
    ordering_fields = ['id', 'intensity', 'year']


class FiltersView(views.APIView):
    def get(self, request, *args, **kwargs):
        qs = InsightEntry.objects.all()
        data = {
            'topics': [t for t in qs.values_list('topic', flat=True).distinct().order_by('topic') if t],
            'sectors': [s for s in qs.values_list('sector', flat=True).distinct().order_by('sector') if s],
            'regions': [r for r in qs.values_list('region', flat=True).distinct().order_by('region') if r],
            'countries': [c for c in qs.values_list('country', flat=True).distinct().order_by('country') if c],
            'cities': [c for c in qs.values_list('city', flat=True).distinct().order_by('city') if c],
            'pestles': [p for p in qs.values_list('pestle', flat=True).distinct().order_by('pestle') if p],
            'sources': [s for s in qs.values_list('source', flat=True).distinct().order_by('source') if s],
            'swots': [s for s in qs.values_list('swot', flat=True).distinct().order_by('swot') if s],
            'years': [y for y in qs.values_list('year', flat=True).distinct().order_by('year') if y],
        }
        return Response(data)


class IntensityByYearView(views.APIView):
    def get(self, request, *args, **kwargs):
        qs = InsightEntry.objects.annotate(
            year_val=Coalesce('year', ExtractYear('published'), 2020)
        ).filter(
            year_val__isnull=False,
            intensity__isnull=False
        ).values('year_val').annotate(
            avg_intensity=Avg('intensity'),
            count=Count('id')
        ).order_by('year_val')

        results = [{
            'year': int(row['year_val']),
            'avg_intensity': round(float(row['avg_intensity']) or 0, 1),
            'count': int(row['count'])
        } for row in qs]
        return Response(results)


class LikelihoodTrendView(views.APIView):
    def get(self, request, *args, **kwargs):
        qs = InsightEntry.objects.annotate(
            year_val=Coalesce('year', ExtractYear('published'), 2020)
        ).filter(
            year_val__isnull=False,
            likelihood__isnull=False
        ).values('year_val').annotate(
            avg_likelihood=Avg('likelihood')
        ).order_by('year_val')

        results = [{
            'year': int(row['year_val']),
            'avg_likelihood': round(float(row['avg_likelihood']) or 0, 1),
        } for row in qs]
        return Response(results)