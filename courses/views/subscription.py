from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from courses.models import Subscription
from courses.serializers.subscription import SubscriptionSerializer


class SubscriptionCreateView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    '''def perform_create(self, serializer):
        print('ДО СЮДА ДОХОДИТ')
        obj = serializer.save()
        obj.user = self.request.user
        obj.save()'''

    def post(self, request, **kwargs):
        data = request.data.copy()
        user = request.user.pk
        print('USER', user)
        data.update({'course': kwargs['course_id'], 'user': user})
        data['user'] = user
        print(data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
