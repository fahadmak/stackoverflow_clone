from django.test import TestCase
from django.urls import reverse
from questions.models import Question
from accounts.models import User

from votes.models import QuestionVote


class TestVoteView(TestCase):

    def setUp(self):
        self.credentials = {
            'display_name': 'testuser',
            'email': 'testuser',
            'username': 'testuser',
            'password': 'secret'}
        self.user = User.objects.create_user(**self.credentials)
        self.question = Question.objects.create(
            title=f'Christian',
            author=self.user
        )

    def test_question_up_voted(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

        # down vote a question
        self.client.get(reverse('votes:down_vote', kwargs={'question_id': self.question.id}))

        # up vote a question
        response2 = self.client.get(reverse('votes:up_vote', kwargs={'question_id': self.question.id}))
        self.assertTrue(QuestionVote.objects.filter(question=self.question, user=self.user))
        self.assertFalse(
            QuestionVote.objects.filter(question=self.question, user=self.user, vote=QuestionVote.VOTE.downVote))

        # up vote a question
        response3 = self.client.get(reverse('votes:up_vote', kwargs={'question_id': self.question.id}))
        self.assertFalse(QuestionVote.objects.filter(question=self.question, user=self.user))

        self.assertEqual(response3.status_code, 302)

    def test_question_down_voted(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

        # up vote a question
        self.client.get(reverse('votes:up_vote', kwargs={'question_id': self.question.id}))

        # down vote a question
        response2 = self.client.get(reverse('votes:down_vote', kwargs={'question_id': self.question.id}))
        self.assertTrue(QuestionVote.objects.filter(question=self.question, user=self.user))
        self.assertFalse(
            QuestionVote.objects.filter(question=self.question, user=self.user, vote=QuestionVote.VOTE.upVote))
        response3 = self.client.get(reverse('votes:down_vote', kwargs={'question_id': self.question.id}))
        self.assertFalse(QuestionVote.objects.filter(question=self.question, user=self.user))
        self.assertEqual(response3.status_code, 302)
