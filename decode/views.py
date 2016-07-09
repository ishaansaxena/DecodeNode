from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")

def question(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)