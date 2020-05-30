from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm


def index(request):
    todo_list = Todo.objects.all()
    form = TodoForm()
    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo/index.html', context)


@require_POST
def addtodo(request):
    form = TodoForm(request.POST)
    if form.is_valid:
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')
