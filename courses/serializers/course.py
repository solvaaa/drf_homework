from rest_framework import serializers

from courses.models import Course, Lesson, Subscription
from courses.serializers.lesson import LessonSerializer
from users.permissions import IsOwner, IsSuperUser, IsModerator


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(source="courses", many=True, read_only=True)
    subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = ('owner',)
        permission_classes = [IsOwner, IsModerator, IsSuperUser]

    def get_lesson_count(self, instance):
        return Lesson.objects.filter(course=instance).count()

    def get_subscribed(self, instance):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        try:
            subscription = Subscription.objects.get(user=user, course=instance)
        except Subscription.DoesNotExist:
            subscription = None
        if subscription is not None:
            return subscription.is_subscribed
        return False
