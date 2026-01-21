from django import forms
from .models import TrainingRecord


class RecordForm(forms.ModelForm):
    class Meta:
        model = TrainingRecord
        fields = ['date', 'training_type', 'duration', 'feeling', 'memo']
