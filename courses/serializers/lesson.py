from rest_framework import serializers

from courses.models import Lesson
from courses.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        read_only_fields = ('owner', )
        validators = [UrlValidator(field='video_url')]
