from celery import shared_task
from datetime import datetime, timedelta
import requests
from django.conf import settings
from .models import Habit


@shared_task
def send_telegram_reminder():
    bot_token = settings.TELEGRAM_BOT_TOKEN
    base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    time_now = datetime.now().time()
    time_start_task = datetime.now() - timedelta(minutes=1)

    habits_to_remind = Habit.objects.filter(time__gte=time_start_task.time(), time__lte=time_now)

    for habit in habits_to_remind:
        chat_id = habit.user.profile.telegram_chat_id
        text = f'Напоминание о выполнении привычки {habit.action} в {habit.time} в {habit.location}'

        data = {
            "chat_id": chat_id,
            "text": text
        }
        requests.post(base_url, data=data)
