from .models import Answer
from rest_framework import status
from rest_framework import generics
from .serializers import AnswerDataSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404


class ListAnswers(generics.ListAPIView):
    serializer_class = AnswerDataSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AnswerDataSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateAnswer(generics.CreateAPIView):
    serializer_class = AnswerDataSerializer
    permission_classes = [IsAuthenticated]


    def post(self, request, format=None):
        serializer = AnswerDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateorDeleteAnswer(generics.UpdateAPIView):
    serializer_class = AnswerDataSerializer

    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = AnswerDataSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

