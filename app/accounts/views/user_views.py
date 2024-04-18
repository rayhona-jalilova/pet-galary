from django.conf import settings
from django.utils.translation import gettext_lazy as _

from rest_framework.generics import (
    RetrieveUpdateAPIView,
    CreateAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from accounts.serializers import UserProfileSerializer, LoginSerializer


class UserProfileView(RetrieveUpdateAPIView):
    """Manage authenticated user."""

    queryset = settings.AUTH_USER_MODEL
    serializer_class = UserProfileSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(self):
        """Retrieve and return authenticated user."""
        return self.request.user


class LoginView(ObtainAuthToken):
    """Login View."""

    serializer_class = LoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class LogoutView(APIView):
    """
    View for user logout using token auth.
    """

    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Delete the user's token from database."""
        request.auth.delete()
        msg = _("Logout successfully")
        return Response({"details": msg}, status=200)


class UserCreateView(CreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [
        AllowAny,
    ]


class AuthenticationCheckView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(
            {"detail": _("User Authenticated")}, status=status.HTTP_200_OK
        )
