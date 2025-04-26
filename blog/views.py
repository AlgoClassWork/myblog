# Логика для страниц: что показывать и как обрабатывать данные

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import Post, Comment, Like
from .forms import CommentForm, EmailForm

# Главная страница: список всех постов
def post_list(request):
    posts = Post.objects.all()  # Берем все посты из базы
    favorites = request.session.get('favorites', [])  # Избранные посты из сессии
    return render(request, 'blog/list.html', {'posts': posts, 'favorites': favorites})

# Страница поста: показывает пост и комментарии
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  # Находим пост по ID или показываем ошибку
    comments = Comment.objects.filter(post=post)  # Все комментарии к посту
    comment_form = CommentForm()  # Пустая форма для нового комментария
    favorites = request.session.get('favorites', [])  # Избранные посты

    # Если пользователь отправил комментарий
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)  # Заполняем форму данными
        if comment_form.is_valid():  # Проверяем, всё ли правильно
            new_comment = comment_form.save(commit=False)  # Создаём комментарий, но не сохраняем
            new_comment.post = post  # Привязываем к посту
            new_comment.save()  # Сохраняем
            comment_form = CommentForm()  # Очищаем форму

    return render(request, 'blog/detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'favorites': favorites
    })

# Страница отправки поста по email
def post_share(request, id):
    post = get_object_or_404(Post, id=id)  # Находим пост
    form = EmailForm()  # Пустая форма
    favorites = request.session.get('favorites', [])  # Избранные посты

    # Если пользователь отправил форму
    if request.method == 'POST':
        form = EmailForm(request.POST)  # Заполняем данными
        if form.is_valid():  # Проверяем
            data = form.cleaned_data  # Берем данные
            post_url = request.build_absolute_uri(f'/post/{post.id}/')  # Ссылка на пост
            subject = f"{data['name']} советует пост"  # Тема письма
            message = f"Прочитай пост: {post.title}\nСсылка: {post_url}\nСообщение: {data['message']}"
            send_mail(subject, message, 'from@example.com', [data['to']])  # Отправляем
            form = EmailForm()  # Очищаем форму

    return render(request, 'blog/share.html', {'post': post, 'form': form, 'favorites': favorites})

# Поставить лайк посту
def post_like(request, id):
    post = get_object_or_404(Post, id=id)  # Находим пост
    ip_address = request.META.get('REMOTE_ADDR')  # Получаем IP пользователя

    # Проверяем, не лайкал ли уже пользователь
    if not Like.objects.filter(post=post, ip_address=ip_address).exists():
        Like.objects.create(post=post, ip_address=ip_address)  # Создаём лайк

    return redirect('post_detail', id=id)  # Возвращаемся на страницу поста

# Список избранных постов
def favorites_list(request):
    favorites = request.session.get('favorites', [])  # Получаем ID избранных постов
    posts = Post.objects.filter(id__in=favorites)  # Находим посты по ID
    return render(request, 'blog/favorites.html', {'posts': posts, 'favorites': favorites})

# Добавить или удалить пост из избранного
def toggle_favorite(request, id):
    post = get_object_or_404(Post, id=id)  # Находим пост
    favorites = request.session.get('favorites', [])  # Получаем текущий список

    if id in favorites:
        favorites.remove(id)  # Удаляем из избранного
    else:
        favorites.append(id)  # Добавляем в избранное

    request.session['favorites'] = favorites  # Сохраняем в сессии
    return redirect('post_detail', id=id)  # Возвращаемся на страницу поста
