from drf_playground.files.models import Details
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


class FileSerializer(serializers.ModelSerializer):
    owner_first_name = SerializerMethodField()
    owner_last_name = SerializerMethodField()

    class Meta:
        model = Details
        fields = ["name", "permissions", "owner_first_name", "owner_last_name"]

    def get_owner_first_name(self, details: Details):
        return details.owner.user.first_name

    def get_owner_last_name(self, details: Details):
        return details.owner.user.last_name
