from django import forms

from parser.models import TVParser


class ParserForm(forms.Form):

    def parser_data(self):
        films_parser = parser()
        items_to_create = []
        for i in films_parser:
            post = TVParser(**i)
            items_to_create.append(i)
        TVParser.objects.bulk_create(items_to_create)