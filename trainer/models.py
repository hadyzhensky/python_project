"""Models for SQL Trainer application."""
from django.db import models
from django.contrib.auth.models import User


class SQLTask(models.Model):
    """SQL task for training."""

    title = models.CharField(max_length=200)
    description = models.TextField()
    correct_query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    hint = models.TextField(blank=True)

    def __str__(self) -> str:
        """Return task title."""
        return self.title


class HistoricalEvent(models.Model):
    """Historical event for sample database."""

    year = models.IntegerField()
    event = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    notable_person = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        """Return event description."""
        return f"{self.year} — {self.event} ({self.country})"


class UserProgress(models.Model):
    """Track user's progress in completing tasks."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey("SQLTask", on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    class Meta:
        """Meta options for UserProgress."""

        unique_together = ("user", "task")
