from django.db import models

# The Feed model represents an RSS feed
class Feed(models.Model):
    url = models.URLField(unique=True) #url
    title = models.CharField(max_length=255) #title
    description = models.TextField(blank=True) #description 
    last_fetched = models.DateTimeField(null=True, blank=True) #date of data retrieval

    def __str__(self):
        return self.title

# The FeedItem model represents an item in an RSS feed.
class FeedItem(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='items') #The foreign key linked to the Feed model, each element belongs to a feed
    title = models.CharField(max_length=255)
    link = models.URLField() #The link to the feed element
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField() #The publication date of the feed item
    guid = models.CharField(max_length=255, unique=True) #A unique identifier for the feed element

    def __str__(self):
        return self.title
