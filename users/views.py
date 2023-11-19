from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import UserSerializer, MyTokenObtainPairSerializer
from django.contrib.auth import authenticate, login as django_login, logout
from rest_framework import status


# Create your views here.

@swagger_auto_schema(
    method='post',
    operation_description="Регистрация нового пользователя",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email пользователя'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Пароль')
        },
        required=['email', 'password']
    ),
    responses={201: openapi.Response('Пользователь успешно зарегистрирован')}
)
@api_view(['POST'])
def register_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='post',
    operation_description="Авторизация пользователя",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email пользователя'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Пароль')
        },
        required=['email', 'password']
    ),
    responses={200: openapi.Response('Успешная авторизация'), 401: 'Неверные учетные данные'}
)
@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)
    if user:
        django_login(request, user)
        return Response({'message': 'Успешная авторизация'}, status=status.HTTP_200_OK)
    return Response({'message': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    method='post',
    operation_description="Выход пользователя из системы",
    responses={200: openapi.Response('Вы успешно вышли из системы')}
)
@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Вы успешно вышли из системы"}, status=status.HTTP_200_OK)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
