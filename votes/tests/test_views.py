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
        self.assertTrue(QuestionVote.objects.filter(question=self.question, voter=self.user))
        self.assertFalse(
            QuestionVote.objects.filter(question=self.question, voter=self.user, vote=QuestionVote.VOTE.downVote))

        # up vote a question
        response3 = self.client.get(reverse('votes:up_vote', kwargs={'question_id': self.question.id}))
        self.assertFalse(QuestionVote.objects.filter(question=self.question, voter=self.user))

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
        self.assertTrue(QuestionVote.objects.filter(question=self.question, voter=self.user))
        self.assertFalse(
            QuestionVote.objects.filter(question=self.question, voter=self.user, vote=QuestionVote.VOTE.upVote))
        response3 = self.client.get(reverse('votes:down_vote', kwargs={'question_id': self.question.id}))
        self.assertFalse(QuestionVote.objects.filter(question=self.question, voter=self.user))
        self.assertEqual(response3.status_code, 302)

    # def test_lists_all_answers(self):
    #     # Get second page and confirm it has (exactly) remaining 3 items
    #     self.client.post('/accounts/login/', self.credentials, follow=True)
    #     response = self.client.get(reverse('answers:answer_list', kwargs={'question_id': self.question.id}))
    #     print(self.question.id)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(len(response.context['answer_list']) == 14)

    # def test_answer_comment_created(self):
    #     # send login data
    #     response = self.client.post('/accounts/login/', self.credentials, follow=True)
    #     # should be logged in now
    #     self.assertTrue(response.context['user'].is_active)
    #
    #     response3 = self.client.post(
    #         reverse('answers:answer_detail', kwargs={'answer_id': self.answer.id, 'question_id': self.question.id}),
    #         {'answer_comment': 'titles'})
    #     print(response3)
    #     self.assertEqual(len(mail.outbox), 1)
    #     self.assertEqual(response3.status_code, 302)
    #
    # def test_lists_all_comments(self):
    #     # Get second page and confirm it has (exactly) remaining 3 items
    #     self.client.post('/accounts/login/', self.credentials, follow=True)
    #     response = self.client.get(reverse('answers:answer_list', kwargs={'question_id': self.question.id}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(len(response.context['question_comments']) == 13)
    #
    # def test_answer_comment_failed_to_be_created(self):
    #     # send login data
    #     response = self.client.post('/accounts/login/', self.credentials, follow=True)
    #     # should be logged in now
    #     self.assertTrue(response.context['user'].is_active)
    #
    #     response3 = self.client.post(
    #         reverse('answers:answer_detail', kwargs={'answer_id': self.answer.id, 'question_id': self.question.id}),
    #         {'answer_comment': ''})
    #     print(response3)
    #     self.assertTemplateUsed(response3, 'questions/question_detail.html')
