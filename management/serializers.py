from rest_framework import serializers

from management.models import Circular, Event, Planner, Management


class CircularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circular
        fields = ('id', 'title', 'date', 'sender', 'description')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'venue', 'incharge', 'time', 'phone', 'department', 'description')


class PlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planner
        fields = ('id', 'name', 'url')


class ManagementSerializer(serializers.ModelSerializer):
    planner = PlannerSerializer(many=True)
    event = EventSerializer(many=True)
    circular = CircularSerializer(many=True)

    class Meta:
        model = Management
        fields = ('id', 'year', 'department', 'planner', 'event', 'circular')