from rest_framework import serializers
from CV_ables_api.models import Project
from CV_ables_api.serializers import ApplicantSmallSerializer

class ProjectSerializer(serializers.ModelSerializer):
    applicant = ApplicantSmallSerializer(many=False)
    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'github_url',
            'deploy_url',
            'image_url',
            'applicant'
        )