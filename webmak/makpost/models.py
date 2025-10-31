from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

COLLEGE_CHOICES = [
    
    ('cedat', 'CEDAT'),
    ('cocis', 'COCIS'),
    ('chs', 'CHS'),
    ('cobams', 'COBAMS'),
    ('conas', 'CONAS'),
    ('chuss', 'CHUSS'),
    ('caes', 'CAES'),
    ('cees', 'CEES'),
    ('covab', 'COVAB')
]

#A user can belong to one college only
class CustomUser(AbstractUser):
    name = models.CharField(max_length=250, null = True, blank=True)
    college = models.CharField(max_length=20, choices=COLLEGE_CHOICES, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="profiles/", blank=True, null=True)
    email = models.EmailField(unique=True)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['college']

    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.email}"


#every post belongs to a user and a college and they can post in any college they want
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    college = models.CharField(max_length=20, choices=COLLEGE_CHOICES)   # user can override
    title = models.CharField(max_length = 200, blank=True, null = True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    video = models.FileField(upload_to="videos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.college}"
    
    def comment_count(self):
        return self.comments.count()

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on Post {self.post.id}"
    

