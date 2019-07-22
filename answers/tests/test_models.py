from django.test import TestCase
from accounts.models import User
from answers.models import Answer
from questions.models import Question


class TestQuestionModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="faga@gh.com",
            username="username",
            display_name="username",
            password="Philo1234")
        self.question = Question.objects.create(title="title", author=self.user)

    def test_title(self):
        answer = Answer.objects.create(
            answer_title="faga@ghs.com",
            author=self.user,
            question=self.question,
            )
        self.assertEquals(answer.answer_title, "faga@ghs.com")
