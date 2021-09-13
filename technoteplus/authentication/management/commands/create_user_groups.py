from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission,Group

PERMISSIONS = ['add_note', 'change_note', 'delete_note', 'view_note', 'view_tag','add_tag','add_sharednote','view_sharednote']
class Command(BaseCommand):
    '''
    Creating superuser programatically
    '''

    def handle(self, *args, **options):
      try:
          base_group, created = Group.objects.get_or_create(name='base')
          if  created:
            for permission in PERMISSIONS:
                model_add_perm = Permission.objects.get(codename=permission)
                base_group.permissions.add(model_add_perm)

      except Exception as e:
          print('%s (%s)' % (str(e), type(e)))

