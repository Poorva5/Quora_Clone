from django.contrib import admin
from .models import Answer


@admin.register(Answer)
class AnswerDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'author']
    search_fields = [ 'author']
