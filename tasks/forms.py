from django import forms
from django.utils.translation import ugettext

from tasks.models import Task, Variable


class TaskForm(forms.ModelForm):

    name = forms.CharField(max_length=30, help_text='Name of task', label=ugettext('Name:'))
    text = forms.CharField(max_length=3000, help_text='Text of task', label=ugettext('Text:'))
    formula = forms.CharField(max_length=256, help_text='Formula for answer', label=ugettext('Formula:'))

    class Meta:
        model = Task
        fields = ('name', 'text', 'formula')


class VariablesForm(forms.ModelForm):

    name = forms.CharField(max_length=6, label=ugettext('Name:'))
    value = forms.FloatField(label=ugettext('Value:'))

    class Meta:
        model = Variable
        fields = ('name', 'value')
