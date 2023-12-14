from django_filters.rest_framework import (
    FilterSet,
    CharFilter,
    NumberFilter,
)

from reviews.models import Title


class TitleFilter(FilterSet):
    genre = CharFilter(field_name='genre__slug')
    category = CharFilter(field_name='category__slug')
    year = NumberFilter(field_name='year')
    name = CharFilter(field_name='name')

    class Meta:
        model = Title
        fields = ('year', 'name',)