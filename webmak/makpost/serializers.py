from rest_framework import serializers
from .models import CustomUser, Profile, Post, Comment

# -----------------------------
# Profile Serializer
# -----------------------------
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio']


# -----------------------------
# User Serializer
# -----------------------------
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'college', 'profile_pic', 'profile']


# -----------------------------
# Comment Serializer
# -----------------------------
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


# -----------------------------
# Post Serializer
# -----------------------------
class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['user', 'college', 'title', 'content', 'created_at', 'comments', 'comment_count', 'image', 'video']
        read_only_fields = ['created_at', 'comments', 'comment_count', 'user']

    def get_comment_count(self, obj):
        return obj.comments.count()


# -----------------------------
# Profile Page Serializer (User + Only Their Posts)
# -----------------------------
class ProfilePageSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    posts = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'college', 'profile_pic', 'profile', 'posts']

    def get_posts(self, obj):
        # Only posts for this user
        posts = Post.objects.filter(user=obj).order_by('-created_at')
        return PostSerializer(posts, many=True).data
