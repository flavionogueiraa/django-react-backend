from rest_framework import permissions, viewsets

from ..models import List
from ..serializers import ListSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
