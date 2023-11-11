from .models import Task, Bet
from django.forms import ModelForm, widgets, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {'title': TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Введите название'}),
                   'task': Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Введите описание'}),
                   }

class BetForm(ModelForm):
    class Meta:
        model = Bet
        fields = ["title", "body"]
        widgets = {'title': TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Введите название'}),
                   'body': Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Введите описание'}),
                   }

