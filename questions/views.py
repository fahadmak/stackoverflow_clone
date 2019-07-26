from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.db.models.functions import Lower
from django.shortcuts import render_to_response, render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from answers.models import Answer
from votes.models import QuestionVote
from .forms import CreateQuestionForm
from .models import Question, QuestionComment, Tag


class QuestionView(LoginRequiredMixin, CreateView, ListView):
    login_url = reverse_lazy("accounts:login")
    form_class = CreateQuestionForm
    success_url = reverse_lazy("questions:question_list")
    template_name = 'questions/index.html'

    def form_valid(self, form):
        tags = form.cleaned_data['tag'].split(',')
        form.instance.author = self.request.user
        form.instance.save()
        for tag in tags:
            tag_exists = Tag.objects.filter(name=tag)
            if tag_exists:
                old_tag = tag_exists[0]
                form.instance.tags.add(old_tag)
            else:
                new_tag = Tag.objects.create(name=tag)
                form.instance.tags.add(new_tag)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        question_votes = QuestionVote.objects.all()
        answers = Answer.objects.all()
        question_comments = QuestionComment.objects.all()
        tags = Tag.objects.all()

        if len(tags) >= 10:
            tags = tags[:10]

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

        for tag in tags:
            if tag.name in request.GET:
                questions = questions.filter(tags=tag)

        context = {
            'questions': questions,
            'question_votes': question_votes,
            'answers': answers,
            'form': form,
            'question_comments': question_comments,
            'tags': tags}

        return render(request, 'questions/index.html', context)
