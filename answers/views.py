from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from stackoverflow import settings
from .models import Question, Answer, AnswerComment
from questions.models import QuestionComment
from answers.forms import CreateAnswerForm, CreateAnswerCommentForm
from questions.forms import CreateQuestionCommentForm


class AnswerView(LoginRequiredMixin, TemplateView):
    template_name = 'questions/question_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = get_object_or_404(Question, pk=kwargs['question_id'])
        # Add in a QuerySet of all the books
        context['question'] = question
        context['question_comments'] = QuestionComment.objects.filter(question=question).order_by('-created_at')
        context['answer_comments'] = AnswerComment.objects.all().order_by('-created_at')
        # context['question_comments'] = QuestionComment.objects.filter(question=question).order_by('-created_at')
        context['answer_list'] = Answer.objects.filter(question=question).order_by('-created_at')
        context['answer_form'] = CreateAnswerForm(self.request.POST or None, prefix='aform_pre')
        context['comment_form'] = CreateQuestionCommentForm(self.request.POST or None, prefix='cform_pre')
        context['answer_comment_form'] = CreateAnswerCommentForm(self.request.POST or None, prefix='acform_pre')

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        answer_form = context['answer_form']
        comment_form = context['comment_form']
        answer_comment_form = context['answer_comment_form']
        question_id = kwargs['question_id']
        domain = f'http://127.0.0.1:8000/{question_id}/answers/'
        if answer_form.is_valid():
            new_answer = answer_form.save(commit=False)
            new_answer.author = self.request.user
            new_answer.question = context['question']
            new_answer.save()
            send_mail('Your question has been answered',
                      f"Your question \'{context['question'].title}\' has received an answer. Click  to see {domain}",
                      settings.EMAIL_HOST_USER,
                      [context['question'].author.email])
            return HttpResponseRedirect(reverse('answers:answer_list', kwargs={'question_id': kwargs['question_id']}))

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = self.request.user
            new_comment.question = Question.objects.get(id=kwargs['question_id'])
            new_comment.save()
            send_mail('Your question has been commented on',
                      f"Your question \'{context['question'].title}\' has received a comment. Click  to see {domain}",
                      settings.EMAIL_HOST_USER,
                      [context['question'].author.email])
            return HttpResponseRedirect(reverse('answers:answer_list', kwargs={'question_id': kwargs['question_id']}))

        if answer_comment_form.is_valid():
            new_comment = answer_comment_form.save(commit=False)
            new_comment.author = self.request.user
            new_comment.answer = Answer.objects.get(id=kwargs['answer_id'])
            new_comment.save()
            return HttpResponseRedirect(reverse('answers:answer_list', kwargs={'question_id': kwargs['question_id']}))
        return self.render_to_response({'aform': answer_form})
