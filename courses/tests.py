from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Lesson, Course, Subscription
from users.models import User

LESSON_DATA = {
    "name": "Tester",
    "description": "TestCase",
    "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
}
COURSE_DATA = {
    "name": "ТестКурс",
    "description": "Тестовый курс 2"
}


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@mail.ru',
            first_name='Test',
            last_name='Test',
        )
        self.user.set_password('11qwerty11')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create(self):
        data = LESSON_DATA

        response = self.client.post(
            '/lesson/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': 1, 'name': 'Tester', 'description': 'TestCase', 'preview': None,
             'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
             'course': None, 'owner': self.user.id}
        )
        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_delete(self):
        data = LESSON_DATA
        Lesson.objects.create(owner=self.user, **data)
        lesson_id = Lesson.objects.first().id

        response = self.client.delete(
            f'/lesson/delete/{lesson_id}'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertFalse(
            Lesson.objects.all().exists()
        )

    def test_list(self):
        data = LESSON_DATA
        lesson = Lesson.objects.create(owner=self.user, **data)

        response = self.client.get(
            '/lesson/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': lesson.id, 'name': 'Tester', 'description': 'TestCase', 'preview': None,
                 'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'course': None,
                 'owner': self.user.id}]}

        )

    def test_update(self):
        data = LESSON_DATA
        data['name'] = 'tester2'
        lesson = Lesson.objects.create(owner=self.user, **data)
        lesson_id = lesson.id

        response = self.client.put(
            f'/lesson/edit/{lesson.id}',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertTrue(
            Lesson.objects.all().exists()
        )
        self.assertEqual(
            response.json(),
            {'id': lesson.id, 'name': 'tester2', 'description': 'TestCase', 'preview': None,
             'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'course': None, 'owner': self.user.id}
        )

    def test_retrieve(self):
        data = LESSON_DATA
        lesson = Lesson.objects.create(owner=self.user, **data)

        response = self.client.get(
            f'/lesson/{lesson.id}'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'id': lesson.id, 'name': 'Tester', 'description': 'TestCase', 'preview': None,
             'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'course': None, 'owner': self.user.id}
        )


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@mail.ru',
            first_name='Test',
            last_name='Test',
        )
        self.user.set_password('11qwerty11')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_subscribe(self):
        course = Course.objects.create(**COURSE_DATA, owner=self.user)

        response = self.client.post(
            f'/course/{course.pk}/subscribe/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': 1, 'is_subscribed': True, 'user': self.user.id, 'course': course.id}
        )
        self.assertTrue(
            Subscription.objects.all().exists()
        )

        retrieve_response = self.client.get(
            f'/course/{course.pk}/'
        )
        self.assertTrue(
            retrieve_response.json()['subscribed']
        )

    def test_unsubscribe(self):
        course = Course.objects.create(owner=self.user, **COURSE_DATA)
        subscription = Subscription.objects.create(user=self.user,
                                                   course=course,
                                                   is_subscribed=True)

        response = self.client.delete(
            f'/course/{course.id}/unsubscribe/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertFalse(
            Subscription.objects.all().exists()
        )

        retrieve_response = self.client.get(
            f'/course/{course.pk}/'
        )
        self.assertFalse(
            retrieve_response.json()['subscribed']
        )
