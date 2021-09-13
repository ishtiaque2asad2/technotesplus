from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    '''
    Creating superuser programatically
    '''

    def handle(self, *args, **options):
        try:
            if len(get_user_model().objects.filter(username='admin')) == 0:
                get_user_model().objects.create_superuser(username='admin',
                                                          password='admin',
                                                          email='admin@admin.com',
                                                          first_name="admin",
                                                          last_name="admin"
                                                          )
        except Exception as e:
            print('%s (%s)' % (str(e), type(e)))
