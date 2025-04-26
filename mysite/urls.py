# Это главные маршруты сайта — какие страницы открывать

from django.contrib import admin
from django.urls import path, include

# Список маршрутов
urlpatterns = [
    path('admin/', admin.site.urls),  # Админ-панель по адресу /admin/
    path('', include('blog.urls')),   # Все маршруты блога начинаются с /
]
