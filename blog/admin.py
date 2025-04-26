# Настройки админ-панели, чтобы управлять постами, комментариями и лайками

from django.contrib import admin
from .models import Post, Comment, Like

# Регистрируем посты
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'like_count']  # Добавляем лайки
    search_fields = ['title', 'body']                           # Поиск по заголовку и тексту

    def like_count(self, obj):
        return obj.like_count()  # Показываем количество лайков
    like_count.short_description = 'Лайки'  # Название столбца

# Регистрируем комментарии
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created']    # Что показывать
    search_fields = ['name', 'body']              # Поиск по имени и тексту

# Регистрируем лайки
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'ip_address', 'created']  # Показываем пост и IP
    search_fields = ['ip_address']                   # Поиск по IP
