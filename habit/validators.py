from django.core.exceptions import ValidationError


def validate_habit_reward_and_related_habit(habit):
    if habit.related_habit and habit.reward:
        raise ValidationError("Нельзя одновременно выбирать связанную привычку и указывать вознаграждение.")


def validate_habit_duration(habit):
    if habit.duration.total_seconds() > 120:
        raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


def validate_related_habit_pleasant(habit):
    if habit.related_habit and not habit.related_habit.is_pleasant:
        raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки.")


def validate_pleasant_habit_restrictions(habit):
    if habit.is_pleasant and (habit.reward or habit.related_habit):
        raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


def validate_habit_frequency(habit):
    if habit.frequency > 7:
        raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
