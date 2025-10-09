from rest_framework import serializers
from .models import Stickers, Boards, Users, Threads, Comments


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = ['board_name']
