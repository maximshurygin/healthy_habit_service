from rest_framework import serializers
from .models import Habit
from .validators import (
    validate_habit_reward_and_related_habit,
    validate_habit_duration,
    validate_related_habit_pleasant,
    validate_pleasant_habit_restrictions,
    validate_habit_frequency
)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, attrs):
        habit = Habit(**attrs)

        validate_habit_reward_and_related_habit(habit)
        validate_habit_duration(habit)
        validate_related_habit_pleasant(habit)
        validate_pleasant_habit_restrictions(habit)
        validate_habit_frequency(habit)

        return attrs


class PublicHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'location', 'time', 'action', 'frequency', 'duration', 'is_public']
        read_only_fields = fields
