import feedparser
from datetime import datetime
from .models import Feed, FeedItem

def parse_feed(feed: Feed):
    # Analyzes RSS feeds by URL
    parsed = feedparser.parse(feed.url)

    # Checks for malformed flux
    if parsed.bozo:
        raise ValueError("Flux non valide")

    # Updates general feed information
    feed.title = parsed.feed.get('title', feed.url)
    feed.description = parsed.feed.get('description', '')
    feed.last_fetched = datetime.now()
    feed.save()

    # Browse articles in the feed
    for entry in parsed.entries:
        # Uses the unique identifier (guid) to avoid duplication
        guid = entry.get('id', entry.get('link'))
        # Creates a new item only if it doesn't already exist
        if not FeedItem.objects.filter(guid=guid).exists():
            FeedItem.objects.create(
                feed=feed,
                title=entry.get('title', 'Sans titre'),
                link=entry.get('link', ''),
                description=entry.get('summary', ''),
                pub_date=entry.get('published_parsed') and datetime(*entry.published_parsed[:6]),
                guid=guid
            )
