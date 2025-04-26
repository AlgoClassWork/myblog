# Маршруты для страниц блога

from django.urls import path
from . import views

# Список маршрутов
urlpatterns = [
    path('', views.post_list, name='post_list'),            # Главная: список постов
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Страница поста
    path('post/<int:id>/share/', views.post_share, name='post_share'),  # Отправка поста
    path('post/<int:id>/like/', views.post_like, name='post_like'),  # Поставить лайк
    path('favorites/', views.favorites_list, name='favorites_list'),  # Список избранного
    path('post/<int:id>/favorite/', views.toggle_favorite, name='toggle_favorite'),  # Добавить/удалить избранное
]
