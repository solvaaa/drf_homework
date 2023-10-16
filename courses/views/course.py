from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from courses.models import Course
from courses.paginators import MyPagination
from courses.serializers.course import CourseSerializer
from users.models import UserRoles
from users.permissions import IsOwner, IsSuperUser, IsModerator


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination

    def create(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.permission_classes = [IsOwner | IsSuperUser]
        return super().update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.permission_classes = [IsOwner | IsModerator | IsSuperUser]
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [IsOwner | IsSuperUser]
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        obj = serializer.save()
        obj.owner = self.request.user
        obj.save()
