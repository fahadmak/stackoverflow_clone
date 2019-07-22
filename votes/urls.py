from django.urls import path

from votes.views import UpVote, DownVote

app_name = 'votes'

urlpatterns = [
    path('up-vote/<int:question_id>/', UpVote.as_view(), name="up_vote"),
    path('down-vote/<int:question_id>/', DownVote.as_view(), name="down_vote"),
]
