from django.test import TestCase
from questions.forms import CreateQuestionForm


class TestCreateQuestionForm(TestCase):

    def test_forms(self):
        form_data = {'title': 'Hello'}
        form = CreateQuestionForm(data=form_data)
        self.assertTrue(form.is_valid())