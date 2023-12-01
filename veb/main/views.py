from django.shortcuts import render, redirect
from .models import Task, Bet
from .forms import TaskForm, BetForm

def index(request):
    tasks = Task.objects.all()
    context = {'title': 'Главная страница', 'tasks': tasks}
    return render(request, 'index.html', context)
def about(request):
    bet = Bet.objects.all()
    return render(request, 'about.html', {'bet': bet})
def teacher(request):
    return render(request, 'teacher.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Не верно введен текст'
    form = TaskForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)
