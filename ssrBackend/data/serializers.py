from rest_framework import serializers
from .models import Project,teamDetails


class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["projectId", "name", "description", "year", "mentor","category",'youtubeLink','img']


class teamDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = teamDetails
        fields = ["roll", "name", "projectId"]


