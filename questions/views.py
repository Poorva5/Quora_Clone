from .models import Question
from rest_framework import status
from rest_framework import generics
from .serializers import QuestionDataSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404


class ListQuestions(generics.ListAPIView):
    serializer_class = QuestionDataSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuestionDataSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateQuestions(generics.CreateAPIView):
    serializer_class = QuestionDataSerializer
    permission_classes = [IsAuthenticated]


    def post(self, request, format=None):
        serializer = QuestionDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateorDeleteQuestion(generics.UpdateAPIView):
    serializer_class = QuestionDataSerializer

    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionDataSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












