from django_filters  import rest_framework as filters
from simpleapp.models import Snippet

class SnippetFilter(filters.FilterSet):

    class Meta:
        model = Snippet
        fields = {
            'title': ['icontains'],
            'body': ['icontains'],
            'created': ['iexact', 'lte', 'gte'],
        }

