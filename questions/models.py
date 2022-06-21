from django.db import models
from account.models import UserData


class Question(models.Model):
    author = models.ForeignKey(UserData, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





