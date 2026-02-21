from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from .serializers import RegisterSerializer, LoginSerializer
from django.shortcuts import get_object_or_404
from .models import User as CustomUser



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
  

class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)

        if request.user == user_to_follow:
            return Response(
                {"error": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.add(user_to_follow)

        return Response(
            {"message": f"You are now following {user_to_follow.username}"},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

        request.user.following.remove(user_to_unfollow)

        return Response(
            {"message": f"You unfollowed {user_to_unfollow.username}"},
            status=status.HTTP_200_OK
        )
