from django_filters import rest_framework as filters
from .models import InsightEntry


class InsightEntryFilter(filters.FilterSet):
    """
    FilterSet defines which query parameters are allowed.
    We use MultipleChoice-like filters via BaseInFilter for multi-value.
    """

    # Multi-value filters: ?topic=oil&topic=gas
    topic = filters.BaseInFilter(field_name='topic', lookup_expr='in')
    sector = filters.BaseInFilter(field_name='sector', lookup_expr='in')
    region = filters.BaseInFilter(field_name='region', lookup_expr='in')
    country = filters.BaseInFilter(field_name='country', lookup_expr='in')
    city = filters.BaseInFilter(field_name='city', lookup_expr='in')
    pestle = filters.BaseInFilter(field_name='pestle', lookup_expr='in')
    source = filters.BaseInFilter(field_name='source', lookup_expr='in')
    swot = filters.BaseInFilter(field_name='swot', lookup_expr='in')

    # Simple numeric filters
    start_year = filters.NumberFilter(field_name='start_year', lookup_expr='gte')
    end_year = filters.NumberFilter(field_name='end_year', lookup_expr='lte')

    # Date range filters on published date
    published_from = filters.DateFilter(field_name='published', lookup_expr='gte')
    published_to = filters.DateFilter(field_name='published', lookup_expr='lte')

    class Meta:
        model = InsightEntry
        fields = [
            'topic',
            'sector',
            'region',
            'country',
            'city',
            'pestle',
            'source',
            'swot',
            'start_year',
            'end_year',
            'published_from',
            'published_to',
        ]
