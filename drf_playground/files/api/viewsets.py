from drf_playground.files.api.serializers import FileSerializer
from drf_playground.files.models import Details
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet


class FileViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    queryset = Details.objects.all()

    serializer_class = FileSerializer

    def get_serializer_class(self):
        return FileSerializer
