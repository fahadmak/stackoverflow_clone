from django import template

from votes.models import QuestionVote

register = template.Library()


@register.filter(name='get_up_votes')
def get_up_votes(question_votes, question):
    question_up_votes = question_votes.filter(question=question, vote=QuestionVote.VOTE.upVote)
    return question_up_votes


@register.filter(name='get_down_votes')
def get_down_votes(question_votes, question):
    question_down_votes = question_votes.filter(question=question, vote=QuestionVote.VOTE.downVote)
    return question_down_votes