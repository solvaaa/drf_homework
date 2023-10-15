from rest_framework import serializers

from courses.models import Course, Lesson
from courses.serializers.lesson import LessonSerializer
from users.permissions import IsOwner, IsSuperUser, IsModerator


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(source="courses", many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = ('owner',)
        permission_classes = [IsOwner, IsModerator, IsSuperUser]

    def get_lesson_count(self, instance):
        return Lesson.objects.filter(course=instance).count()
