from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def index(req):
    latest_questions_list = Question.objects.order_by('pub_date')[:5]
    context = {
            'latest_questions_list': latest_questions_list
            }
    return render(req, 'polls/index.html', context)


def detail(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/detail.html', {'question': question})


def results(req, question_id):
    res = f'You are looking at results of question {question_id}'
    return HttpResponse(res)


def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(req, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,))
            )
