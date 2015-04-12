from django.shortcuts import render

from .models import Question
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))