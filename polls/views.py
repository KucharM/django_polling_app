from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice


def home(request):
    question_list = Question.objects.all()
    context = {
        'question_list': question_list,
    }
    return render(request, 'polls/home.html', context)
