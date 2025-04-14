from django.core.management.base import BaseCommand
from feeds.models import Feed
from feeds.rss_parser import parse_feed

#Define custom command for RSS feed updates
class Command(BaseCommand):
    help = 'Met à jour tous les flux RSS' #Description of the commande

    def handle(self, *args, **kwargs):# The handle method is executed when the
    # We browse all RSS feeds, attempt to update them with the parse_feed function and display a success or error message depending on the result of the operation.
        for feed in Feed.objects.all():
            try:
                parse_feed(feed)
                self.stdout.write(self.style.SUCCESS(f'Mis à jour : {feed.title}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Erreur pour {feed.url} : {e}'))
