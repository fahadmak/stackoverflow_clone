from django.urls import path
from .views import AnswerView

app_name = 'questions'

urlpatterns = [
    path('', AnswerView.as_view(), name='answer_list'),
    path('<int:answer_id>/', AnswerView.as_view(), name='answer_detail'),
]

