from rest_framework import serializers

from api.models import Link


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'created', 'url', 'upvotes', 'downvotes', 'score']

