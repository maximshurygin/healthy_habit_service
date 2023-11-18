from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Habit
from .serializers import HabitSerializer, PublicHabitSerializer
from .permissions import IsOwnerOrReadOnly
from .pagination import SmallPagination


class PrivateHabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = SmallPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PublicHabitsListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PublicHabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = SmallPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)
