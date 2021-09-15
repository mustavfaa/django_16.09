from django_filters import rest_framework as filters
from .models import smartphone


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ShoppFilter(filters.FilterSet):    
    genres = CharFilterInFilter(field_name='category__name', lookup_expr='in')
    price = filters.RangeFilter()
    class Meta:
        model = smartphone
        fields = ['genres', 'price']








