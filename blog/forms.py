from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """Form for comment submission on blog posts.

    Reference: https://youtu.be/dm1MToEiXuw
    """
    class Meta:
        # The model to use
        model = Comment
        # Which fields to display
        fields = ('body',)
