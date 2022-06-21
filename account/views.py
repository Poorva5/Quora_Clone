from rest_framework.generics import CreateAPIView
from . import serializers, models
from helper import keys
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny


class RegisterView(CreateAPIView):
    serializer_class =serializers.UserSerializer
    model = serializer_class.Meta.model

    def create(self, request, *args, **kwargs):
        password = request.POST.get(keys.PASSWORD, None)
        if password:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                user.set_password(password)
                user.save()
                serializer = self.get_serializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Password Required'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    # authentication_classes = (TokenAuthentication)
    # permission_classes = (AllowAny,)

    def get(self, request):
        user = models.UserData.objects.get(id=request.user.id)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)




        







