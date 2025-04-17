from django.db import models

from users.models import Profile


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(upload_to="profile/images")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile.user.username}"

    @property
    def like_count(self):
        return self.likes.count()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="liked_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            "post",
            "profile",
        )  # Ensures a user can like a post only once

    def __str__(self):
        return f"{self.profile.user.username} liked {self.post}"


class Conversation(models.Model):
    participants = models.ManyToManyField(Profile)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation between: {', '.join([p.user.username for p in self.participants.all()])}"


class Message1(models.Model):
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="messages"
    )
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.sender.user.username}: {self.content[:20]}"


class Notification(models.Model):
    receiver_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="notification_messages"
    )
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.receiver_profile}"
