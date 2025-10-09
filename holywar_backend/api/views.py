from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from .models import Stickers, Boards, Users, Threads, Comments
from .serializers import UsersSerializer


@api_view(['GET'])
def user_dump(request):
    all_users = Users.objects.all()
    users_ser = UsersSerializer(all_users, many=True)
    return Response(users_ser.data)
