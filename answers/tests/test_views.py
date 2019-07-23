from django.test import TestCase
from django.urls import reverse
from questions.models import Question, QuestionComment
from accounts.models import User
from answers.models import Answer
from django.core import mail


class TestAnswerView(TestCase):

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
        self.answer = Answer.objects.create(
            answer_title=f'Christian',
            author=user,
            question=self.question
        )
        number_of_answers = 13

        for author_id in range(number_of_answers):
            Answer.objects.create(
                answer_title=f'Christian {author_id}',
                author=user,
                question=self.question
            )

        for author_id in range(number_of_answers):
            QuestionComment.objects.create(
                question_comment=f'Christian {author_id}',
                author=user,
                question=self.question
            )

    def test_answer_created(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

        response3 = self.client.post(reverse('answers:answer_list', kwargs={'question_id': self.question.id}),
                                     {'answer_title': 'titles'})
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(response3.status_code, 302)

    def test_lists_all_answers(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        self.client.post('/accounts/login/', self.credentials, follow=True)
        response = self.client.get(reverse('answers:answer_list', kwargs={'question_id': self.question.id}))
        print(self.question.id)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['answer_list']) == 14)

    def test_answer_comment_created(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

        response3 = self.client.post(
            reverse('answers:answer_detail', kwargs={'answer_id': self.answer.id, 'question_id': self.question.id}),
            {'answer_comment': 'titles'})
        print(response3)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(response3.status_code, 302)

    def test_lists_all_comments(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        self.client.post('/accounts/login/', self.credentials, follow=True)
        response = self.client.get(reverse('answers:answer_list', kwargs={'question_id': self.question.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['question_comments']) == 13)

