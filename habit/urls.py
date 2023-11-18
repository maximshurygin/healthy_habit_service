from habit.apps import HabitConfig
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrivateHabitViewSet, PublicHabitsListView

app_name = HabitConfig.name

router = DefaultRouter()
router.register(r'private-habits', PrivateHabitViewSet, basename='private-habit')
router.register(r'public-habits', PublicHabitsListView, basename='public-habit')

urlpatterns = [
    path('', include(router.urls)),
]
