from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    '''
    Creating superuser programatically
    '''

    def handle(self, *args, **options):
        base_group = Group.objects.get(name='base')
        try:
            if len(get_user_model().objects.filter(username='whitney')) == 0:
                user = get_user_model().objects.create_user(
                    username='whitney',
                    password='whitney',
                    first_name='Whitney',
                    last_name='Tucker',
                    email='whitney@technoteplus.com',
                )
                # Assign user to group with CRUD for Notes and readonly for Tags model
                base_group.user_set.add(user)
        except Exception as e:
            print('%s (%s)' % (str(e), type(e)))

        try:
            if len(get_user_model().objects.filter(username='scott')) == 0:
                user = get_user_model().objects.create_user(
                    username='scott',
                    password='scott',
                    first_name='Scott',
                    last_name='Hampton',
                    email='scott@technoteplus.com',
                )
                base_group.user_set.add(user)
        except Exception as e:
            print('%s (%s)' % (str(e), type(e)))
