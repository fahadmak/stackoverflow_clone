from django.db import models
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Question(models.Model):
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    @property
    def num_votes(self):
        return self.questionvote_set.count()


class QuestionComment(models.Model):
    question_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

