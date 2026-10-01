from django import forms
from .models import StudyTask

class StudyTaskForm(forms.ModelForm):
    """Create a form from the StudyTask database model."""
    class Meta:
        model = StudyTask
        fields = ["subject", "title", "minutes"]
        widgets = {
            "subject": forms.TextInput(attrs={"placeholder": "Example: CSE 310"}),
            "title": forms.TextInput(attrs={"placeholder": "Example: Learn Django forms"}),
            "minutes": forms.NumberInput(attrs={"min": 5, "max": 600}),
        }
