from django import forms
from .models import Answer

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        # Pop the current question from kwargs
        current_question = kwargs.pop('question', None)
        super().__init__(*args, **kwargs)
        if current_question:
            # Build choices based on Answer objects for the current question
            choices = [(answer.id, answer.text) for answer in Answer.objects.filter(question=current_question)]
            self.fields['answer'] = forms.ChoiceField(
                choices=choices,
                widget=forms.RadioSelect,  # This renders radio buttons
                label=current_question.text
            )
        else:
            # If no question is provided, you can add a default field or leave it empty
            self.fields['answer'] = forms.ChoiceField(
                choices=[],
                widget=forms.RadioSelect,
                label="No question available"
            )
