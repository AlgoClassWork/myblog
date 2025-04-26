# Это главные настройки нашего сайта

import os
from pathlib import Path

# Папка, где лежит наш проект
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ для безопасности (в продакшене храним в переменной окружения)
SECRET_KEY = 'django-insecure-verysecretkey123'

# Режим разработки (True — для тестов, False — для реального сайта)
DEBUG = True

# Какие домены могут обращаться к сайту (пустой список = любой)
ALLOWED_HOSTS = []

# Наши приложения (blog — это наше приложение, остальное — встроенное в Django)
INSTALLED_APPS = [
    'django.contrib.admin',      # Админ-панель
    'django.contrib.auth',       # Система пользователей
    'django.contrib.contenttypes',
    'django.contrib.sessions',   # Сессии для пользователей
    'django.contrib.messages',   # Сообщения об успехе/ошибках
    'django.contrib.staticfiles', # Поддержка CSS и картинок
    'blog',                      # Наше приложение
]

# Программы, которые обрабатывают запросы
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Поддержка сессий
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Главный файл маршрутов
ROOT_URLCONF = 'simple_blog.urls'

# Настройки шаблонов (где искать HTML-файлы)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Для запуска сервера
WSGI_APPLICATION = 'simple_blog.wsgi.application'

# База данных (используем SQLite — простая база, файл на компьютере)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Проверка паролей (оставляем по умолчанию)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Язык и часовой пояс
LANGUAGE_CODE = 'ru-ru'  # Русский язык
TIME_ZONE = 'UTC'        # Универсальное время

# Поддержка разных языков
USE_I18N = True
USE_TZ = True

# Где лежат CSS и картинки
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Какой тип первичного ключа использовать
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки для отправки email (выводим письма в консоль для простоты)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Настройки сессий
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Сохраняем сессии в базе
SESSION_COOKIE_AGE = 1209600  # Сессия живёт 2 недели
