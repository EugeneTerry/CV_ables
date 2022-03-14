from rest_framework import serializers
from CV_ables_api.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'github_url',
            'deploy_url',
            'image_url'
        )