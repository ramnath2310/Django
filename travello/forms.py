from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  # This matches the Comment model's text field

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  # This should also use the Comment model's text field
