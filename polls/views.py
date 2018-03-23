from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question


from django.template import loader

def index(request):

    ques_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list':
            ques_list,
    }
    return HttpResponse(render(request, 'polls/index.html', context))




# Display question text with no result but with a form to vote
def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html',  {'question': question})

# Results - display results for particular question
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# Vote Action - Handle voting for a particular choice
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
