from django.contrib import admin

from .models import Users, Stickers, Boards, Threads, Comments

admin.site.register(Users)
admin.site.register(Stickers)
admin.site.register(Boards)
admin.site.register(Threads)
admin.site.register(Comments)
