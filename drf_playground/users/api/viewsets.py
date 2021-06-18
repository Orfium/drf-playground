from django.contrib.auth import get_user_model
from drf_playground.users.api.serializers import (
    UserReadSerializer,
    UserSerializer,
)
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

User = get_user_model()


class UserViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ["me", "list", "retrieve"]:
            return UserReadSerializer
        return UserSerializer

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
