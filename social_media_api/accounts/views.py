from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from .serializers import RegisterSerializer, LoginSerializer

#Register View
class RegisterView(generics.CreateAPIView):
  serializer_class = RegisterSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = self.serializer_class.Meta.model.objects.get(
      username=response.data['username']
    )
    token = Token.objects.get(user=user)
    return Response({
      "user": response.data,
      "token": token.key
    })

#Login View
class LoginView(APIView):
  def post(self, request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data
    token, _ = Token.objects.get_or_create(user=user)

    return Response({
      "token": token.key
    }, status=status.HTTP_200_OK)