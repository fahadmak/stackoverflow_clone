from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.db.models.functions import Lower
from django.shortcuts import render_to_response, render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from answers.models import Answer
from votes.models import QuestionVote
from .forms import CreateQuestionForm
from .models import Question, QuestionComment


class QuestionView(LoginRequiredMixin, CreateView, ListView):
    login_url = reverse_lazy("accounts:login")
    form_class = CreateQuestionForm
    success_url = reverse_lazy("questions:question_list")
    template_name = 'questions/index.html'

    # model = Question

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        question_votes = QuestionVote.objects.all()
        answers = Answer.objects.all()
        question_comments = QuestionComment.objects.all()
        form = CreateQuestionForm

        if 'top' in request.GET:
            questions = questions.order_by(Lower('title'))

        if 'pub_date' in request.GET:
            questions = questions.order_by('-created_at')

        if 'hot' in request.GET:
            questions = questions.annotate(Count('questionvote', )).filter(
                questionvote__vote=QuestionVote.VOTE.upVote).order_by('-questionvote__count')
        if 'featured' in request.GET:
            questions = questions.annotate(Count('answer', )).order_by('-answer__count')

        context = {'questions': questions, 'question_votes': question_votes, 'answers': answers, 'form': form,
                   'question_comments': question_comments}
        return render(request, 'questions/index.html', context)
