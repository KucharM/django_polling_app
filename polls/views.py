from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice


def home(request):
    question_list = Question.objects.all()
    context = {
        'question_list': question_list,
    }
    return render(request, 'polls/home.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

    except Question.DoesNotExist:
        raise Http404('question not exists')

    context = {
        'question': question,
    }
    return render(request, 'polls/details.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)