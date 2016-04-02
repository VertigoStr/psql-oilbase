from django.core.management.base import BaseCommand
from oilbase.models import Products

class Command(BaseCommand):
    def handle(self, *args, **options):
        Products.objects.all().delete()