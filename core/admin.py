from django.contrib import admin
from django.contrib.admin import register
from .models import Post, Profile, Like


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'image',)


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_time')


@register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')


