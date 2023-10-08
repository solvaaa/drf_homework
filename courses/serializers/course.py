from rest_framework import serializers

from courses.models import Course


class CourseSerializer(serializers):
    class  Meta:
        model = Course
        fields = "__all__"
