from django.core import mail
from django.test import TestCase
from django.urls import reverse
from questions.models import Question
from accounts.models import User


class TestQuestionView(TestCase):

    def setUp(self):
        self.credentials = {
            'display_name': 'testuser',
            'email': 'testuser',
            'username': 'testuser',
            'password': 'secret'}
        user = User.objects.create_user(**self.credentials)
        self.question = Question.objects.create(
            title=f'Christian',
            author=user
        )
        number_of_questions = 13

        for author_id in range(number_of_questions):
            Question.objects.create(
                title=f'Christian {author_id}',
                author=user
            )

    def test_question_created(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

        response2 = self.client.post(reverse('questions:question_list'),
                                     {'title': 'title', 'tag': 'tags,yut'})
        self.assertRedirects(response2, reverse('questions:question_list'))

    def test_lists_all_questions(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        self.client.post('/accounts/login/', self.credentials, follow=True)
        response = self.client.get(reverse('questions:question_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['questions']) == 14)

    def test_question_comment_created(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

        response3 = self.client.post(
            reverse('answers:answer_list', kwargs={'question_id': self.question.id}),
            {'question_comment': 'titles'})
        print(response3)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(response3.status_code, 302)
