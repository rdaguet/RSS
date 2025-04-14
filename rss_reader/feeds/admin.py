from django.contrib import admin
from .models import Feed, FeedItem

#Feed model registration in the administration interface
@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'last_fetched')

#FeedItem template registration in the administration interface
@admin.register(FeedItem)
class FeedItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'feed', 'pub_date')
    list_filter = ('feed',)# list_filter adds a filter to the 'feed' field in the admin interface
