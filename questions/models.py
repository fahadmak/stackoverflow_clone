from django.db import models


class Question(models.Model):
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)