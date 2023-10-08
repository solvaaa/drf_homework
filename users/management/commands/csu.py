from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='alexandrasolovjova@mail.ru',
            first_name='Admin',
            last_name='Project',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('11qwerty11')
        user.save()
