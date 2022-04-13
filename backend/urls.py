from rest_framework import routers

from .views import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
