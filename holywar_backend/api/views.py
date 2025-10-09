from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, viewsets
from .models import Stickers, Boards, Users, Threads, Comments
from .serializers import UsersSerializer, BoardsSerializer, ThreadsSerializer


class HomePage(APIView):
    def get(self, request, format=None):
        all_users = Users.objects.all()
        users_ser = UsersSerializer(all_users, many=True)
        return Response(users_ser.data)


class ListBoards(APIView):

    def get(self, request, format=None):
        all_boards = Boards.objects.all()
        boards_ser = BoardsSerializer(all_boards, many=True)
        return Response(boards_ser.data)


class ThreadList(APIView):

    def get(self, request, url_board, url_board_page=1, format=None):
        page_offset = 10 * (url_board_page - 1)
        page_start = 0 + page_offset
        page_end = 10 + page_offset
        # this huge ORM request gets newest threads starting from page_start to page_end
        thread_page = Threads.objects.filter(board_name__board_name=url_board).order_by(
            '-time_of_creation')[page_start:page_end]
        threads_ser = ThreadsSerializer(thread_page, many=True)
        return Response(threads_ser.data)
