from django.shortcuts import render

from tasks.forms import TaskForm, VariablesForm


def createTask(request):
    context = dict()
    context['task'] = TaskForm
    context['variables'] = VariablesForm
    return render(request, 'tasks/create.html', context)
