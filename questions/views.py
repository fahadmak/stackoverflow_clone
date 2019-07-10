from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from questions.forms import CreateQuestionForm


class QuestionView(TemplateView):
    template_name = 'questions/index.html'

    def post(self, request):
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateQuestionForm()
            return redirect(reverse("questions:question_list"))
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
