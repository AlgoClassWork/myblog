from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm

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