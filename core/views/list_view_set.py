from rest_framework import authentication, permissions, viewsets

from ..models import List
from ..serializers import ListSerializer


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication
    ]

    def get_queryset(self):
        user = self.request.user
        return List.objects.filter(owner=user)
