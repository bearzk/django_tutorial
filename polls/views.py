from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('you are at polls index')
def detail(request, question_id):
    return HttpResponse('you are looking at question %s.' % question_id)

def results(request, question_id):
    response = 'you are looking at %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('you are looking at question %s' % question_id)
