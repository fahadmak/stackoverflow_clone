from django.db import models

from questions.models import Question
from stackoverflow import settings
from model_utils import Choices


class QuestionVote(models.Model):
    VOTE = Choices('upVote', 'downVote')
    vote = models.CharField(choices=VOTE, default=VOTE.upVote, max_length=20)
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
