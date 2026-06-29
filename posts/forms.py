from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Form for creating post"""

    class Meta:
        """Configuration for the post"""

        model = Post
        fields = ("content", "post_picture")

        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 3, "placeholder": "What's on your mind?"}
            )
        }

    def clean(self):
        cleaned_data = super().clean()

        content = cleaned_data.get("content")
        image = cleaned_data.get("post_picture")

        if content:
            content = content.strip()

        if not content and not image:
            raise forms.ValidationError("Add text or an image.")

        return cleaned_data


class CommentForm(forms.ModelForm):
    """Comments Form"""

    class Meta:
        """Configuration for the comments"""

        model = Comment
        fields = ("content",)

        widgets = {
            "content": forms.TextInput(attrs={"placeholder": "Write a comment..."})
        }
