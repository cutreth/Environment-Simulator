from django.shortcuts import render
from django.http import HttpResponse


def api(request):
    response = HttpResponse('Hello world!')
    return response
