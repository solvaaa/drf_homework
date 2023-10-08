from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView

from courses.models import Lesson
from courses.serializers.lesson import LessonSerializer


class LessonDetailView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonListView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyView(DestroyAPIView):
    pass
