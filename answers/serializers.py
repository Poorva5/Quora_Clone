from . import models
from rest_framework import serializers


class AnswerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ["author", "question", "body", "created_at", "modified_at"]

