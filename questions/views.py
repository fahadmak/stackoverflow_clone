from django.views.generic import ListView, CreateView
from .forms import CreateQuestionForm
from .models import Question


class QuestionView(CreateView, ListView):
    form_class = CreateQuestionForm
    success_url = '/'
    template_name = 'questions/index.html'
    model = Question
