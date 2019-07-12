from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .forms import CreateQuestionForm
from .models import Question


class QuestionView(LoginRequiredMixin, CreateView, ListView):
    login_url = '/accounts/login/'
    form_class = CreateQuestionForm
    success_url = '/'
    template_name = 'questions/index.html'
    model = Question
