from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.base import View

from questions.models import Question
from votes.models import QuestionVote


class UpVote(View):
    def get(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['question_id'])
        down_vote = QuestionVote.objects.filter(vote=QuestionVote.VOTE.downVote, user=self.request.user,
                                                question=question)
        if down_vote:
            down_vote.delete()

        up_vote = QuestionVote.objects.filter(vote=QuestionVote.VOTE.upVote, user=self.request.user,
                                              question=question)

        if up_vote:
            up_vote.delete()

        else:
            QuestionVote.objects.create(user=self.request.user, question=question)
        return HttpResponseRedirect(reverse('answers:answer_list', kwargs={'question_id': kwargs['question_id']}))


class DownVote(View):
    def get(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['question_id'])
        up_vote = QuestionVote.objects.filter(vote=QuestionVote.VOTE.upVote, user=self.request.user,
                                              question=question)
        if up_vote:
            up_vote.delete()

        down_vote = QuestionVote.objects.filter(vote=QuestionVote.VOTE.downVote, user=self.request.user,
                                                question=question)
        if down_vote:
            down_vote.delete()
        else:
            QuestionVote.objects.create(user=self.request.user, vote=QuestionVote.VOTE.downVote, question=question)
        return HttpResponseRedirect(reverse('answers:answer_list', kwargs={'question_id': kwargs['question_id']}))
