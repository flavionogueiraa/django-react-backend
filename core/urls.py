from django.urls import include, path
from rest_framework import routers

from .views import ListViewSet

router = routers.DefaultRouter()
router.register(r'list', ListViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
