from rest_framework import serializers

from courses.models import Course, Lesson
from courses.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="courses", many=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_lesson_count(self, instance):
        return Lesson.objects.filter(course=instance).count()


