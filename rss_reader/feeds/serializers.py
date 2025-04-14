from rest_framework import serializers
from .models import Feed, FeedItem

# Serializer for FeedItem object
class FeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedItem
        fields = '__all__'

# Feed object serializer
class FeedSerializer(serializers.ModelSerializer):
    items = FeedItemSerializer(many=True, read_only=True)

    class Meta:
        model = Feed
        fields = '__all__'
