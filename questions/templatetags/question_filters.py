from django import template

register = template.Library()


@register.filter(name='get_question_comments')
def get_question_comments(question_comments, question):
    question_comments = question_comments.filter(question=question)
    return question_comments