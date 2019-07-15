from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from tasks.forms import TaskForm, VariablesForm
from tasks.models import Task, Variable


@login_required
def createTask(request):
    context = dict()
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        variables_form = VariablesForm(request.POST)
        if task_form.is_valid() and variables_form.is_valid():
            task = Task(user=request.user, **task_form.cleaned_data)
            task.save()

            variables = Variable(task=task, **variables_form.cleaned_data)
            variables.save()
    else:
        task_form = TaskForm()
        variables_form = VariablesForm()


    context['task'] = task_form
    context['variables'] = variables_form
    return render(request, 'tasks/create.html', context)
