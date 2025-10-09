from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from .models import Stickers, Boards, Users, Threads, Comments
from .serializers import UsersSerializer, BoardsSerializer


@api_view(['GET'])
def user_dump(request):
    all_users = Users.objects.all()
    users_ser = UsersSerializer(all_users, many=True)
    return Response(users_ser.data)


@api_view(['GET'])
def get_boards(request):
    all_boards = Boards.objects.all()
    boards_ser = BoardsSerializer(all_boards, many=True)
    return Response(boards_ser.data)
