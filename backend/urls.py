from rest_framework import routers
from rest_framework.authtoken import views

from .views import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
]
