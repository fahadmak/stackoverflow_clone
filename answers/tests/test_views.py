from django.test import TestCase
from django.urls import reverse
from questions.models import Question
from accounts.models import User
from answers.models import Answer


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
        number_of_answers = 13

        for author_id in range(number_of_answers):
            Answer.objects.create(
                title=f'Christian {author_id}',
                author=user,
                question=self.question
            )

    def test_answer_created(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

        response3 = self.client.post(reverse('answers:answer_list', kwargs={'pk': self.question.id}),
                                     {'title': 'titles'})
        self.assertEqual(response.status_code, 200)

    def test_lists_all_questions(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        self.client.post('/accounts/login/', self.credentials, follow=True)
        response = self.client.get(reverse('answers:answer_list', kwargs={'pk': self.question.id}))
        print(self.question.id)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['answer_list']) == 13)