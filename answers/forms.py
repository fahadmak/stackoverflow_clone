from django import forms
from .models import Answer


class CreateAnswerForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': "form-control",
            'id': "exampleFormControlTextarea1",
            'rows': 3,
            'placeholder': "Answer the question?"
        }
    ))

    class Meta:
        model = Answer
        fields = ('title', )
