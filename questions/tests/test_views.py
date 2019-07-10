from django.test import TestCase
from django.urls import reverse
from ..models import Question


class QuestionViewTest(TestCase):

    def setUp(self):

        number_of_questions = 13

        for author_id in range(number_of_questions):
            Question.objects.create(
                title=f'Christian {author_id}',
            )

    def test_form_is_submitted_when_detail_is_valid(self):
        response = self.client.post(reverse('questions:question_list'),
                                    {'title': 'title'})
        self.assertRedirects(response, reverse('questions:question_list'))

    def test_lists_all_questions(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('questions:question_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['object_list']) == 13)

