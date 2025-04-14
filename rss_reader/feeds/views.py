from rest_framework import generics, status
from rest_framework.response import Response
from .models import Feed, FeedItem
from .serializers import FeedSerializer, FeedItemSerializer
from .rss_parser import parse_feed

# API view for listing existing feeds and adding new ones
class FeedListCreateAPIView(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def perform_create(self, serializer):
        # Save the feed and then try to parse it to retrieve its articles
        feed = serializer.save()
        try:
            parse_feed(feed)
        except Exception as e:
            # If an error occurs during parsing, the stream is deleted.
            feed.delete()
            raise e

# API view to retrieve, update or delete a specific feed
class FeedDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

# API view to retrieve all items in a given feed
class FeedItemsAPIView(generics.ListAPIView):
    serializer_class = FeedItemSerializer

    def get_queryset(self):
        feed_id = self.kwargs['pk']
        # Retrieves articles from the feed, sorting them by descending publication date
        return FeedItem.objects.filter(feed_id=feed_id).order_by('-pub_date')
