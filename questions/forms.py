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

    class Meta:
        model = Question
        fields = ('title', )


class CreateQuestionCommentForm(forms.ModelForm):
    comment = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': "form-control",
            'id': "exampleFormControlTextarea1",
            'rows': 3,
            'placeholder': "Comment on this question"
        }
    ))

    class Meta:
        model = QuestionComment
        fields = ('comment', )
