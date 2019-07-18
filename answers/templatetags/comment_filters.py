from django import template
from ..models import AnswerComment

register = template.Library()


@register.filter(name='get_comments')
def get_comments(answer_comments, answer):
    answer_comments = answer_comments.filter(answer=answer)
    return answer_comments
