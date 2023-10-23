from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from courses.models import Payment, Course
from courses.serializers.payment import PaymentSerializer
import courses.payment as pay


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['course', 'lesson', 'payment_type']
    ordering_fields = ['date_payment', '-date_payment']


class PaymentPayView(APIView):

    def post(self, request, course_id=None):
        course = Course.objects.get(id=course_id)
        price = pay.get_stripe_price(course)
        response = pay.create_session(price)

        return Response({"url": response["url"]})
