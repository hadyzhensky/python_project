from django.db import models

class SQLTask(models.Model):
    title = models.CharField(max_length=200)         # название задачи
    description = models.TextField()                 # описание задачи
    correct_query = models.TextField()               # правильный SQL
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания

    def __str__(self):
        return self.title
