from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "pub_date", "author", "group")
    list_filter = ("pub_date", "group")
    search_fields = ("text",)
    empty_value_display = "-пусто-"


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "description")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)
    empty_value_display = "-пусто-"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "post", "text", "created")
    list_filter = ("created",)
    search_fields = ("text",)
    empty_value_display = "-пусто-"


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "following")
    search_fields = ("user__username", "following__username")
    empty_value_display = "-пусто-"
