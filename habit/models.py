from django.db import models

from users.models import User

# Create your models here.


NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    location = models.CharField(max_length=200, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=200, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL,
                                      **NULLABLE, verbose_name="Связанная привычка")
    frequency = models.IntegerField(default=1, verbose_name='Периодичность в днях')
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение')
    duration = models.DurationField(verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.location}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
