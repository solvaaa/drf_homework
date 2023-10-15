from django.core.management import BaseCommand

from users.models import User, UserRoles


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(3):
            user = User.objects.create(
                email=f'moderator{i}@mail.ru',
                first_name=f'Moderator{i}',
                last_name='Project',
                is_staff=True,
                is_superuser=False,
                role=UserRoles.MODERATOR
            )

            user.set_password('11qwerty11')
            user.save()
