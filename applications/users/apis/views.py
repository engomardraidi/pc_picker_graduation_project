from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from ...core.constants import Constants
from ...core.functions import get_detail_response
from .serializers import UserSerializer
import jwt

@api_view(['POST'])
def login(request):
    username = request.data.get('username', None)
    password = request.data.get('password', None)

    if username is None or password is None:
        return Response(get_detail_response(Constants.LOGIN_INFORMATION_REQUIRED), status=400)

    user = authenticate(request, username=username, password=password)

    if user is None:
        return Response(get_detail_response(Constants.LOGIN_INFORMATION_INCORRECT), status=401)

    refresh_token_object = RefreshToken.for_user(user)
    refresh_token = str(refresh_token_object)
    access_token = str(refresh_token_object.access_token)

    tokens = {
        'username': username,
        'refresh_token': refresh_token,
        'access_token': access_token
    }

    request.session['refresh_token'] = refresh_token
    return Response(tokens)

@api_view(['POST'])
def logout(request):
    if 'refresh_token' in request.session:
        del request.session['refresh_token']
        request.session.modified = True
        return Response(status=200)
    else:
        return Response(status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_account(request, username):
    authorization = request.headers['Authorization']
    authorization = str(authorization).split()
    access_token = authorization[1]

    decode_jwt = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])

    user = User.objects.get(pk=decode_jwt['user_id'])

    return Response(UserSerializer(user).data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)