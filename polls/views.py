from django.shortcuts import render
from django.http import HttpResponse


def index(req):
    return HttpResponse('Toki, ale. Ni li polls index')


def detail(req, question_id):
    return HttpResponse(f'You are looking at question {question_id}')


def results(req, question_id):
    res = f'You are looking at results of question {question_id}'
    return HttpResponse(res)


def vote(req, question_id):
    return HttpResponse(f'You are voting on question {question_id}')
