from simpleapp.views import SnippetViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('snippets', SnippetViewSet, base_name='snippet')