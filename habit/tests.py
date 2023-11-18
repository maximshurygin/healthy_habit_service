from rest_framework.test import APITestCase
from users.models import User
from habit.models import Habit


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='testuser@example.com', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Тестирование создания привычки"""
        data = {
            "location": "Дом",
            "time": "08:00",
            "action": "Чтение",
            "is_pleasant": False,
            "frequency": 1,
            "reward": "Награда",
            "duration": "00:01:00",
        }
        response = self.client.post('/private-habits/', data)
        self.assertEqual(response.status_code, 201)

    def test_list_habits(self):
        """Тестирование отображения списка привычек"""
        Habit.objects.create(
            user=self.user,
            location="Дом",
            action="Чтение",
            time="16:00",
            is_pleasant=False,
            frequency=1,
            reward="Награда",
            duration="00:01:00"
        )
        response = self.client.get('/private-habits/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(habit['action'] == "Чтение" for habit in response.data['results']))

    def test_update_habit(self):
        """Тестирование обновления привычки"""
        habit = Habit.objects.create(
            user=self.user,
            location="Дом",
            action="Чтение",
            time="16:00",
            is_pleasant=False,
            frequency=1,
            reward="Вознаграждение",
            duration="00:01:00"
        )
        data = {
            'location': 'Офис',
            'action': 'Чтение',
            'time': '09:00',
            'is_pleasant': False,
            'frequency': 2,
            'reward': "Новое вознаграждение",
            'duration': '00:01:00',
        }
        response = self.client.put(f'/private-habits/{habit.id}/', data)
        self.assertEqual(response.status_code, 200)

    def test_delete_habit(self):
        """Тестирование удаления привычки"""
        habit = Habit.objects.create(
            user=self.user,
            location="Дом",
            action="Чтение",
            time="08:00",
            is_pleasant=False,
            frequency=1,
            reward="Удовольствие",
            duration="00:01:00"
        )
        response = self.client.delete(f'/private-habits/{habit.id}/')
        self.assertEqual(response.status_code, 204)


class PublicHabitListViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='testuser@example.com', password='testpass')
        self.client.force_authenticate(user=self.user)

        Habit.objects.create(
            user=self.user,
            action='action1',
            time="16:00",
            is_pleasant=False,
            frequency=1,
            reward="Удовольствие",
            duration="00:01:00",
            is_public=True
        )
        Habit.objects.create(
            user=self.user,
            action='action2',
            time="17:00",
            is_pleasant=True,
            frequency=2,
            reward="Удовольствие",
            duration="00:01:00",
            is_public=False
        )
        Habit.objects.create(
            user=self.user,
            action='action3',
            time="18:00",
            is_pleasant=False,
            frequency=3,
            reward="Удовольствие",
            duration="00:01:00",
            is_public=True
        )

    def test_list_public_habits(self):
        """Тестирование получения списка публичных привычек"""
        response = self.client.get('/public-habits/')
        self.assertEqual(response.status_code, 200)
        public_habits = [habit for habit in response.data['results'] if habit['is_public']]
        self.assertEqual(len(public_habits), 2)
