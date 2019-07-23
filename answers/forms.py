from django import forms
from .models import Answer, AnswerComment


class CreateAnswerForm(forms.ModelForm):
    answer_title = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': "form-control",
            'id': "exampleFormControlTextarea1",
            'rows': 3,
            'placeholder': "Answer the question?"
        }
    ))

    class Meta:
        model = Answer
        fields = ('answer_title', )


class CreateAnswerCommentForm(forms.ModelForm):
    answer_comment = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': "form-control",
            'id': "exampleFormControlTextarea1",
            'rows': 3,
            'placeholder': "Comment on this answer"
        }
    ))

    class Meta:
        model = AnswerComment
        fields = ('answer_comment', )
