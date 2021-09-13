from django.core.management.base import BaseCommand
from note.models import Tag
from django.contrib.auth import get_user_model
class Command(BaseCommand):
    def handle(self, *args, **options):
        admin = get_user_model().objects.get(username='admin')
        try:
            Tag.objects.get_or_create(name='Assignment',created_by=admin,updated_by=admin)
            Tag.objects.get_or_create(name='Homework',created_by=admin,updated_by=admin)
            Tag.objects.get_or_create(name='Thesis',created_by=admin,updated_by=admin)
        except Exception as e:
            print('%s (%s)' % (str(e), type(e)))