from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()

class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=2000, blank=True)
    labels = models.CharField(max_length=200, blank=True)
    link = models.URLField(max_length=200, blank=True, unique=False)
    upload = models.FileField(upload_to="uploads/", null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
#    story_date = models.DateField()
#    geolocation = 
    characters = models.CharField(max_length=200)
    media_link = models.URLField(max_length=200, blank=True, unique=False)
    likes = models.ManyToManyField(User, blank=True, related_name="liked_stories")

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ("-created_date",)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    story = models.ForeignKey("stories.Story", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ("created_date",)
        indexes = [
            models.Index(fields=["created_date"]),
        ]

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text