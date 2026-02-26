from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.serializers.user_serializer import (
    UserSerializer,
    UserRegistrationSerializer
)
from apps.user.schema import user_register_schema


class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    @user_register_schema
    def post(self, request):
        if request.user is None or not request.user.is_authenticated:
            serializer = UserRegistrationSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            user = serializer.create(serializer.validated_data)
            refresh = RefreshToken.for_user(user)

            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response(
                data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data={
                "error": "You are logged in"
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class UserInfoView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request):
        serializer = UserSerializer(instance=request.user)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
