"""This module manages all views."""
from django.http import HttpResponse


def index(request):
    """Question “index” page – displays the latest few questions"""
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    """Question “detail” page – displays a question text,
    with no results but with a form to vote.
    """
    return HttpResponse("You're looking at question %s." % question_id)

def result(request, question_id):
    """Question “results” page – displays results for a particular question."""
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """Vote action – handles voting for a particular choice in a particular question."""
    return HttpResponse("You're voting on question %s." % question_id)
