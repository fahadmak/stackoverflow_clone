from django import forms
from .models import Question, QuestionComment


class CreateQuestionForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': "form-control",
            'id': "exampleFormControlTextarea1",
            'rows': 3,
            'placeholder': "What is your question?"
        }
    ))
    tag = forms.CharField(label="Please add or remove a tag on your question", widget=forms.TextInput(
        attrs={
            'class': 'form-control text-secondary',
            'id': 'taga',
            'data-role': 'tagsinput',
            'value': 'science,life,technology,politics'
        }
    ))

    class Meta:
        model = Question
        fields = ('title', )


class CreateQuestionCommentForm(forms.ModelForm):
    question_comment = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': "form-control",
            'id': "exampleFormControlTextarea1",
            'rows': 3,
            'placeholder': "Comment on this question"
        }
    ))

    class Meta:
        model = QuestionComment
        fields = ('question_comment',)
