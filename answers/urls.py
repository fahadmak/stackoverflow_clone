from django.urls import path
from .views import AnswerView

app_name = 'questions'

urlpatterns = [
    path('<int:pk>/', AnswerView.as_view(), name='answer_list'),
]

