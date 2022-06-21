from . import models
from rest_framework import serializers


class QuestionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields =["author", "title", "created_at", "modified_at"]


