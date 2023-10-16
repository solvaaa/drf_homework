from rest_framework import serializers

from courses.models import Subscription, Course


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
