from .models import Comment
from django import forms
from .models import CollaborateRequest


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
