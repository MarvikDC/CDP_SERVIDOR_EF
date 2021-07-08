from rest_framework.response import Response
from .serializers import UserSerializer, UserModelSerializer, UserLoginSerializer #, UserLoginSerializer2
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes

from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response

from django.http.response import JsonResponse

from rest_framework.decorators import api_view, action


@permission_classes((AllowAny, ))
class UserAPI(APIView):
    def post(self, request):
        serializer = UserSerializer( data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

"""
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets


@permission_classes((AllowAny, ))
@csrf_exempt 
class UserViewSet(viewsets.GenericViewSet):
#class UserViewSet(APIView):

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['post'])
    def login(self, request):
        #User sign in.
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
"""


"""
@permission_classes((AllowAny, ))
class LogAPI(APIView):
    def post(self, request):
        serializer = UserLoginSerializer2( data = request.data)
        user=serializer.validate_username(data = request.data)

        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user = user)
            #print(token.key)
            #return Response(token.key)
            #user = serializer.save()
            return JsonResponse(Token.key)
        else:
            return JsonResponse("bad sesion")
#comillas

@permission_classes((AllowAny, ))
class LogAPI(APIView):
    def post(self, request):
        serializer = UserLoginSerializer2( data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user = user)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
            #return JsonResponse(Token.key)
        else:
            #return JsonResponse({"hola"})
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

"""