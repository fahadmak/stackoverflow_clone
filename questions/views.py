from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import CreateQuestionForm
from .models import Question


class QuestionView(LoginRequiredMixin, CreateView, ListView):
    login_url = reverse_lazy("accounts:login")
    form_class = CreateQuestionForm
    success_url = reverse_lazy("questions:question_list")
    template_name = 'questions/index.html'
    model = Question

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
