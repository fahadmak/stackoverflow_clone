from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import get_object_or_404

from .models import Question, Answer
from questions.models import QuestionComment
from answers.forms import CreateAnswerForm
from questions.forms import CreateQuestionCommentForm


class AnswerView(LoginRequiredMixin, TemplateView):
    template_name = 'questions/question_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = get_object_or_404(Question, pk=kwargs['pk'])
        # Add in a QuerySet of all the books
        context['question'] = question
        context['question_comments'] = QuestionComment.objects.filter(question=question).order_by('-created_at')
        context['answer_list'] = Answer.objects.filter(question=question).order_by('-created_at')
        context['answer_form'] = CreateAnswerForm(self.request.POST or None, prefix='aform_pre')
        context['comment_form'] = CreateQuestionCommentForm(self.request.POST or None, prefix='cform_pre')

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        answer_form = context['answer_form']
        comment_form = context['comment_form']

        if answer_form.is_valid():
            new_answer = answer_form.save(commit=False)
            new_answer.author = self.request.user
            new_answer.question = context['question']
            new_answer.save()
            return HttpResponseRedirect(reverse('answers:answer_list', kwargs={'pk': kwargs['pk']}))

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = self.request.user
            new_comment.question = Question.objects.get(id=kwargs['pk'])
            new_comment.save()
            return HttpResponseRedirect(reverse('answers:answer_list', kwargs={'pk': kwargs['pk']}))
        return self.render_to_response({'aform': answer_form})
