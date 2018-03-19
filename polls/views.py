from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Handsome ole you")

# Display question text with no result but with a form to vote
def detail(request, questino_id):
    response = HttpResponse("You're looking at question %s" % questino_id)
    return response

# Results - display results for particular question
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# Vote Action - Handle voting for a particular choice
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
