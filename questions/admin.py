from django.contrib import admin
from .models import Question


@admin.register(Question)
class QuestionDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    search_fields = ['question', 'author']