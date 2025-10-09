from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, viewsets
from .models import Stickers, Boards, Users, Threads, Comments
from .serializers import UsersSerializer, BoardsSerializer, ThreadsSerializer

THREADS_PER_PAGE = 10


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

    def get_threds_ammount(self, board: str):
        return Threads.objects.filter(board).count()

    def calculate_pages(self, curr_page: int, threads_amount: int):
        page_range = 7
        page_distance = page_range//2
        page_arr = []
        for i in range(page_distance):
            # kinda convoluted logic but it is made to adapt to changing page_range number
            # checks if it can go page_range//2 pages back
            page = curr_page - (page_distance - i)
            if page > 0:
                page_arr.append(page)
                page_range -= 1

        page_arr.append(curr_page)
        page_range -= 1
        page = curr_page + 1
        while page_range > 0:
            if (THREADS_PER_PAGE - 1) * page > threads_amount:
                return page_arr
            else:
                page_arr.append(page)
                page += 1

    def get(self, request, url_board, url_board_page=1, format=None):
        page_offset = THREADS_PER_PAGE * (url_board_page - 1)
        page_start = 0 + page_offset
        page_end = THREADS_PER_PAGE + page_offset
        # this huge ORM request gets newest threads starting from page_start to page_end
        thread_page = Threads.objects.filter(board_name__board_name=url_board).order_by(
            '-time_of_creation')[page_start:page_end]
        threads_ser = ThreadsSerializer(thread_page, many=True)
        pages = self.calculate_pages(
            url_board_page, self.get_threds_ammount(url_board))
        # TODO: add serializer to be able to send pages with thread info
        return Response(threads_ser.data)
