from celery import shared_task
from datetime import datetime, timedelta
import requests
from django.conf import settings
from .models import Habit


@shared_task
def send_telegram_reminder():
    """Отправка уведомлений в телеграм"""
    bot_token = settings.TELEGRAM_BOT_TOKEN
    base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    habits = Habit.objects.filter(is_pleasant=False)
    now = datetime.now().date()

    for habit in habits:
        if habit.last_reminder_date is None:
            next_reminder = now
        else:
            next_reminder = habit.last_reminder_date + timedelta(days=habit.frequency)

        if now >= next_reminder:
            chat_id = habit.user.tg_chat_id
            text = f'Напоминание о выполнении привычки {habit.action} в {habit.time} в {habit.location}'
            data = {
                "chat_id": chat_id,
                "text": text
            }
            response = requests.post(base_url, data=data)

            if response.status_code == 200:
                habit.last_reminder_date = now
                habit.save()
                return f"Уведомление отправлено пользователю {habit.user.email}"

            else:
                return f"Ошибка при отправке уведомления пользователю {habit.user.tg_chat_id}: {response.status_code}"
        else:
            return f"Уведомление для пользователя {habit.user.tg_chat_id} не требуется"
