from django.db import models
from django.contrib.auth.models import User

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.text}" - {self.author}'
