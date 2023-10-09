from rest_framework import serializers

from courses.models import Payment
from courses.serializers.course import CourseSerializer
from courses.serializers.lesson import LessonSerializer


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"

