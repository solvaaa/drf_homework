from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from courses.models import Lesson
from courses.paginators import MyPagination
from courses.serializers.lesson import LessonSerializer
from users.permissions import IsOwner, IsModerator, IsSuperUser


class LessonDetailView(RetrieveAPIView):
    """Shows details of the lesson"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner|IsModerator|IsSuperUser]


class LessonListView(ListAPIView):
    """Shows list of available lessons"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()
    pagination_class = MyPagination


class LessonCreateView(CreateAPIView):
    """Creates new lesson"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated & ~IsModerator]

    def perform_create(self, serializer):
        obj = serializer.save()
        obj.owner = self.request.user
        obj.save()


class LessonUpdateView(UpdateAPIView):
    """Modifies lesson"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner | IsModerator | IsSuperUser]


class LessonDestroyView(DestroyAPIView):
    """Deletes lesson"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner | IsSuperUser]
