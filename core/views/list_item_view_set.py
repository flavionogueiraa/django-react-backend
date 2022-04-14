from rest_framework import permissions, viewsets

from ..models import ListItem
from ..serializers import ListItemSerializer


class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
