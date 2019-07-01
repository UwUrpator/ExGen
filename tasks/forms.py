from django import forms

from tasks.models import Task, Variable


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'text', 'formula')


class VariableForm(forms.ModelForm):

    class Meta:
        model = Variable
        fields = ('name', 'value')
