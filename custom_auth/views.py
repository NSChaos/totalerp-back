# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from custom_auth.serializers import UserSerializer
import warnings

class SignIn(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        try:
            credentials = {
                'username': request.data['login'],
                'password': request.data['password']
            }
        except Exception as e:
            warnings.warn("User credentials were not provided\n[%s]: %s" % (type(e), e))
            return Response({'message': 'User credentials were not provided'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(request, **credentials)
        if user is not None:
            login(request, user)
            return Response(UserSerializer(instance=request.user).data)
        else:
            return Response({'message': 'User authentication failed, incorrect login or password'}, status=status.HTTP_409_CONFLICT)


class Profile(APIView):

    permission_classes = []

    def get(self, request):
        if request.user.is_authenticated():
            return Response(UserSerializer(instance=request.user).data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@method_decorator(never_cache, name='dispatch')
class SignOut(APIView):

    permission_classes = []

    def get(self, request):
        response = logout(request)
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie('csrf_token')
        return response