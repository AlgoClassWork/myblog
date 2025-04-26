from django import forms 
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']

class EmailForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    to = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, required=False)
