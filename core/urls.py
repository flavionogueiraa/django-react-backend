from django.urls import include, path
from rest_framework import routers

from .views import ListViewSet, ListItemViewSet

router = routers.DefaultRouter()
router.register(r'list', ListViewSet)
router.register(r'list_item', ListItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
