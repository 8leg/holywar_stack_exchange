from django.db import models
from django.conf import settings


class Stickers(models.Model):
    sticker_name = models.CharField(max_length=100, unique=True)
    sticker_file_addr = models.CharField(max_length=100)


class Boards(models.Model):
    board_name = models.CharField(max_length=100, unique=True)


class Users(models.Model):
    username = models.CharField(max_length=30, unique=True)
    access_level = models.CharField(max_length=30)
    email = models.EmailField()
    passwd = models.CharField(max_length=256)


class Threads(models.Model):
    name = models.CharField(max_length=100)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    author_id = models.ForeignKey(
        Users,
        on_delete=models.SET(settings.DELETED_USER_ID)
    )
    board_name = models.ForeignKey(
        Boards,
        on_delete=models.CASCADE
    )


class Comments(models.Model):
    user_id = models.ForeignKey(
        Users,
        on_delete=models.SET(settings.DELETED_USER_ID)
    )
    thread_id = models.ForeignKey(
        Threads,
        on_delete=models.CASCADE
    )
    time_of_creation = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
