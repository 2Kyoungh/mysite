from django import forms
from bbsnote.models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['subject', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] 
        labels = { 'content':'댓글내용'}
        