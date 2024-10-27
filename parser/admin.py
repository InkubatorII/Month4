from django.contrib import admin
from parser.models import TVParser


@admin.register(TVParser)
class TVParserAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'country', 'duration')

