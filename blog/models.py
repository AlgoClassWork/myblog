# Здесь описываем, какие данные храним в базе (посты, комментарии и лайки)

from django.db import models
from django.contrib.auth.models import User

# Модель поста (заметки в блоге)
class Post(models.Model):
    title = models.CharField(max_length=200)  # Заголовок поста (до 200 букв)
    body = models.TextField()                # Текст поста (любой длины)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE       # Кто написал (если удалить автора, пост тоже удалится)
    )
    created = models.DateTimeField(auto_now_add=True)  # Когда создан (автоматически)

    def __str__(self):
        return self.title  # Показываем заголовок в админке

    # Метод для подсчёта лайков
    def like_count(self):
        return self.likes.count()  # Считаем, сколько лайков у поста

# Модель комментария
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE       # К какому посту относится
    )
    name = models.CharField(max_length=80)   # Имя комментатора
    body = models.TextField()                # Текст комментария
    created = models.DateTimeField(auto_now_add=True)  # Когда оставлен

    def __str__(self):
        return f"Комментарий от {self.name}"  # Показываем, кто написал

# Модель лайка
class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes'  # К какому посту лайк
    )
    ip_address = models.CharField(max_length=45)  # IP-адрес пользователя (для ограничения)
    created = models.DateTimeField(auto_now_add=True)  # Когда поставлен лайк

    def __str__(self):
        return f"Лайк для {self.post.title} от {self.ip_address}"
