from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

@api_view(['POST'])
def login(request):
    username = request.data.get('username', None)
    password = request.data.get('password', None)

    user = authenticate(request, username=username, password=password)

    refresh_token_object = RefreshToken.for_user(user)
    refresh_token = str(refresh_token_object)
    access_token = str(refresh_token_object.access_token)

    tokens = {
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