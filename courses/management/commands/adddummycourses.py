from django.core.management import BaseCommand

from courses.models import Course, Lesson
from random import randint, choice

from users.models import UserRoles, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = list(User.objects.filter(role=UserRoles.MEMBER))
        for i in range(5):
            course = Course.objects.create(
                name=f'Тест курс {i}',
                description=f'Это тестовый курс №{i}',
                owner=choice(users)
            )
            course.save()

        for course in Course.objects.all():
            num_of_lessons = randint(1, 5)
            for i in range(num_of_lessons):
                pk = course.pk
                course_name = course.name
                lesson = Lesson.objects.create(
                    name=f'Тест урок {i}, курс {pk}',
                    description=f'Это тестовый урок №{i} для курса {course_name}',
                    video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                    course=course,
                    owner=course.owner
                )
                lesson.save()

