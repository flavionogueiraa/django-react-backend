from rest_framework import serializers

from ..models import List
from .list_item_serializer import ListItemSerializer


class ListSerializer(serializers.HyperlinkedModelSerializer):
    listitem_set = ListItemSerializer(many=True)

    class Meta:
        model = List
        fields = [
            'url',
            'name',
            'owner',
            'listitem_set',
        ]
