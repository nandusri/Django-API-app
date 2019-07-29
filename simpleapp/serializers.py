from rest_framework import serializers
from simpleapp.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Snippet
        fields = ('title', 'body','created')
        
