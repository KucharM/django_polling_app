from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
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
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question, 
            'error_message': 'please select any choice'}
        return render(request, 'polls/detail.html', context)
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))