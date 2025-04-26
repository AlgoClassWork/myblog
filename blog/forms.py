# Формы для ввода данных (комментарии и отправка по email)

from django import forms
from .models import Comment

# Форма для отправки поста по email
class EmailForm(forms.Form):
    name = forms.CharField(max_length=25)    # Имя отправителя
    to = forms.EmailField()                 # Кому отправить
    message = forms.CharField(widget=forms.Textarea, required=False)  # Сообщение (не обязательно)

# Форма для комментариев
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']  # Только имя и текст
