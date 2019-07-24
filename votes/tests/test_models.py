from django.test import TestCase

from accounts.models import User
from questions.models import Question
from votes.models import QuestionVote


class TestQuestionModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="faga@gh.com",
            username="username",
            display_name="username",
            password="Philo1234")
        self.question = Question.objects.create(title="title", author=self.user)


    def test_questionVote_created(self):
        question_vote = QuestionVote.objects.create(user=self.user, question=self.question)
        self.assertTrue(question_vote.question, self.question)
