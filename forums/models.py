from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    ARMED_FORCES = [
        ("ARMY", "British Army"),
        ("NAVY", "Royal Navy"),
        ("RAF", "Royal Air Force"),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=4, choices=ARMED_FORCES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, max_length=8000)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Author={self.author}, Content={self.content}"
