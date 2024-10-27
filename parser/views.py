from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, FormView

from parser.forms import ParserForm


class FilmView(ListView):
    model = TVParser
    template_name = 'parser/film_list.py'

    def get_queryset(self):
        return TVParser.objects.all()

class ParserView(FormView):
    template_name = 'parser/start_parsing.html'
    form_class = ParserForm

    def post(self, request, *args, **kwargs):
        form = ParserForm(request.POST)
        if not form.is_valid()
