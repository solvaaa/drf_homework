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
    pagination_class = MyPagination
    permission_classes_by_action = {'create': [IsAuthenticated & ~IsModerator],
                                    'list': [IsAuthenticated],
                                    'update': [IsOwner | IsModerator | IsSuperUser],
                                    'partial_update': [IsOwner | IsModerator | IsSuperUser],
                                    'retrieve': [IsOwner | IsModerator | IsSuperUser],
                                    'destroy': [IsOwner | IsSuperUser]
                                    }


    def perform_create(self, serializer):
        obj = serializer.save()
        obj.owner = self.request.user
        obj.save()

    def get_permissions(self, *args, **kwargs):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return super().get_permissions(*args, **kwargs)