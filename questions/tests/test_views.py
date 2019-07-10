from django.test import TestCase
from django.urls import reverse


class QuestionViewTest(TestCase):

    def test_form_is_submitted_when_detail_is_valid(self):
        response = self.client.post(reverse('questions:question_list'),
                                    {'title': 'title'})
        self.assertRedirects(response, reverse('questions:question_list'))
