from rest_framework import serializers
from .models import UserData, Activity

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["start_time", "end_time"]

class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)
    class Meta:
        model = UserData
        fields = ["id", "real_name", "tz", "activity_periods"]
