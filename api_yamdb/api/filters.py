import django_filters
from reviews.models import Title


class TitlesFilter(django_filters.FilterSet):
    genre__slug = django_filters.CharFilter(lookup_expr='iexact')
    category__slug = django_filters.CharFilter()
    year = django_filters.NumberFilter()
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Title
        fields = '__all__'
