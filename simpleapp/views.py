from simpleapp.models import Snippet
from .serializers import SnippetSerializer
from .filters import SnippetFilter
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filterset_class = SnippetFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = ['title','created']


    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)


    @action(methods=['get'], detail=False)
    def oldest(self, request):
        oldest = self.get_queryset().order_by('-created').last()
        serializer = self.get_serializer_class()(oldest)
        return Response(serializer.data)

