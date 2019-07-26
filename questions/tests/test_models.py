from django.test import TestCase
from questions.models import Question, Tag
from accounts.models import User


class TestQuestionModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="faga@gh.com",
            username="username",
            display_name="username",
            password="Philo1234")

    def test_title(self):
        question = Question.objects.create(title="title", author=self.user)
        self.assertEquals(question.title, "title")

    def test_tag_created(self):
        tag = Tag.objects.create(name="title")
        self.assertEquals(tag.name, "title")
