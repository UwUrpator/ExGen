from django import forms

from tasks.models import Task, Variable


class TaskForm(forms.ModelForm):

    name = forms.CharField(max_length=30, help_text='Name of task', label='Name:')
    text = forms.CharField(max_length=3000, help_text='Text of task', label='Text:')
    formula = forms.CharField(max_length=256, help_text='Formula for answer', label='Formula:')

    class Meta:
        model = Task
        fields = ('name', 'text', 'formula')


class VariablesForm(forms.ModelForm):

    class Meta:
        model = Variable
        fields = ('name', 'value')
