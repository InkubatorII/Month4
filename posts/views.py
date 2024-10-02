from django.shortcuts import render
from django.http import HttpResponse
import random


def test_view(request):
    return HttpResponse('Hello world')

def main_page_view(request):
    return HttpResponse(request, 'base.html')

