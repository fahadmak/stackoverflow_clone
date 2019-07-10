from django.test import TestCase
from questions.models import Question


class QuestionModelTest(TestCase):

    def setUp(self):
        Question.objects.create(title="title")

    def test_title(self):
        question = Question.objects.get(id=1)
        self.assertEquals(question.title, "title")
