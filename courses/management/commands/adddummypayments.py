from datetime import datetime, timedelta

from django.core.management import BaseCommand

from courses.models import Lesson, Course, Payment
from users.models import User
from random import sample, randint, choice


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = list(User.objects.all())
        lessons = list(Lesson.objects.all())
        courses = list(Course.objects.all())
        for _ in range(2):
            num_of_users_paid = randint(min(4, len(users)), len(users))
            users_paid = sample(users, num_of_users_paid)
            for user in users_paid:
                choices = choice([lessons, courses])
                paid_for = choice(choices)
                lesson_paid = paid_for if isinstance(paid_for, Lesson) else None
                course_paid = paid_for if lesson_paid is None else None
                payment = Payment.objects.create(
                    user=user,
                    date_payment=datetime.now() - timedelta(days=randint(1, 100), hours=randint(1,23), minutes=randint(1,59)),
                    course=course_paid,
                    lesson=lesson_paid,
                    total=randint(100, 100000),
                    payment_type=choice([Payment.CASH, Payment.CREDIT])
                )
                payment.save()
