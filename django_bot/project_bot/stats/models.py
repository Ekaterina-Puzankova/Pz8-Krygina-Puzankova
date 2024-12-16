

# Create your models here.
from django.db import models
from django.utils import timezone

class Message(models.Model):
    chat_id = models.IntegerField()
    user_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField()
    command = models.CharField(max_length=255, null=True, blank=True) # Добавлено поле для команды
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message from {self.username} at {self.date}"