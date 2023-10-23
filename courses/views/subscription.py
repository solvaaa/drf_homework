from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response

from courses.models import Subscription
from courses.serializers.subscription import SubscriptionSerializer
from users.permissions import IsSubscribedUser


class SubscriptionCreateView(CreateAPIView):
    """Creates subscription for selected course for current user """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    @swagger_auto_schema(
        request_body=no_body
    )
    def post(self, request, **kwargs):
        data = request.data.copy()
        user = request.user.pk
        data.update({'course': kwargs['course_id'], 'user': user})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SubscriptionDeleteView(DestroyAPIView):
    """removes subscription for current user for selected course"""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsSubscribedUser]

    def get_object(self):
        course_id = self.kwargs['course_id']
        user = self.request.user
        obj = Subscription.objects.get(user=user, course=course_id)
        return obj


