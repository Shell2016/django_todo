from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm, TodoModelForm


def index(request):
    todo_list = Todo.objects.all()
    # form = TodoForm()
    form = TodoModelForm()
    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo/index.html', context)


@require_POST
def addtodo(request):
    # form = TodoForm(request.POST)
    form = TodoModelForm(request.POST)
    if form.is_valid():
        # new_todo = Todo(text=form.cleaned_data['text'])
        # new_todo.save()
        form.save()
    return redirect('index')


def complete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.completed = True
    todo.save()
    return redirect('index')


def delcompleted(request):
    Todo.objects.filter(completed=True).delete()
    return redirect('index')


def delall(request):
    Todo.objects.all().delete()
    return redirect('index')
