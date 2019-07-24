from django import template

register = template.Library()


@register.filter(name='get_answer_comments')
def get_answer_comments(answer_comments, answer):
    answer_comments = answer_comments.filter(answer=answer)
    return answer_comments


@register.filter(name='get_answers')
def get_answers(answers, question):
    answers = answers.filter(question=question)
    return answers
