from django.contrib import admin

from .models import Conversation, Like, Message1, Notification, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "profile"]


@admin.register(Like)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "profile"]


@admin.register(Message1)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["id", "conversation_id", "sender", "content"]


admin.site.register(Conversation)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ["id", "receiver_profile", "message"]
