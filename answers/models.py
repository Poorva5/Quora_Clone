from django.db import models
from account import models as account_models
from questions import models as question_models


class Answer(models.Model):
    author = models.ForeignKey(account_models.UserData, on_delete=models.CASCADE)
    question = models.ForeignKey(question_models.Question, on_delete=models.CASCADE)
    body = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body






