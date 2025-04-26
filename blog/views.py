from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Post, Comment
from .forms import CommentForm, EmailForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)
    
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm()

    return render(request, 'blog/detail.html', {
                            'post':post,
                            'comments':comments,
                            'comment_form':comment_form})

def post_share(request, id):
    post = get_object_or_404(Post, id=id)
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post_url = request.build_absolute_uri(f'/post/{post.id}')
            subject = f'{data['name']} советует пост'
            message = f'Прочитай пост {post.title} Ссылка {post_url} Сообщение {data['message']}'
            send_mail(subject, message, 'admin@gmail.com', [data['to']])
            form = EmailForm()

    return render(request, 'blog/share.html', {'post': post, 'form': form})