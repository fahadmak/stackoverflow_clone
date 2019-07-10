from django.urls import path
from .views import QuestionView

app_name = 'questions'

urlpatterns = [
    path('', QuestionView.as_view(), name='question_list'),
]

