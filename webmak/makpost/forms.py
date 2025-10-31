from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser, Post
from django.contrib.auth.forms import UserCreationForm

# --------------------- USER FORM ---------------------
class CustomUserCreationForm(UserCreationForm):
    error_messages = {"password_mismatch":"Passwords don't match"}

    class Meta:
        model = CustomUser
        fields = ["username", "email", "college", "profile_pic","password1", "password2"]


# --------------------- POST FORM ---------------------
MAX_VIDEO_SIZE = 50 * 1024 * 1024  # 50 MB

def validate_video_size(file):
    if file.size > MAX_VIDEO_SIZE:
        raise ValidationError("Video file size must be under 50 MB.")

class PostForm(forms.ModelForm):
    video = forms.FileField(required=False, validators=[validate_video_size])

    class Meta:
        model = Post
        fields = ['college', 'content', 'image', 'video']


# --------------------- COMMENT FORM ---------------------
class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
