from django.urls import path

from users.apps import UsersConfig
from users.views import register_view, login_view, logout_view, MyTokenObtainPairView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
