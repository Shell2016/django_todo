from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from .models import Todo
from django.contrib.auth.models import User
from .forms import TodoModelForm


def index(request):
    if not request.user.is_authenticated:
        context = {}
    else:
        todo_list = Todo.objects.filter(user=request.user)
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
        new_todo = form.save(commit=False)
        new_todo.user = request.user
        new_todo.save()
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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)
