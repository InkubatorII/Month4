from django.shortcuts import render
from django.http import HttpResponse
import random

def main_page_view(request):
    return HttpResponse(random.randint(1,100))

def test_view()
