from django.db import models
from django.contrib.auth.models import User

class SQLTask(models.Model):
    title = models.CharField(max_length=200)         # название задачи
    description = models.TextField()                 # описание задачи
    correct_query = models.TextField()               # правильный SQL
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания
    hint = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class HistoricalEvent(models.Model):
    year = models.IntegerField()
    event = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    notable_person = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.year} — {self.event} ({self.country})"
    
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey('SQLTask', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'task')
