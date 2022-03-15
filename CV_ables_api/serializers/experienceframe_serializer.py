from rest_framework import serializers
from CV_ables_api.models import ExperienceFrame
from CV_ables_api.serializers import FrameworkSerializer
from CV_ables_api.serializers import ProjectSerializer
from CV_ables_api.serializers import ApplicantSmallSerializer
from CV_ables_api.serializers import ExperienceSerializer

class ExperienceFrameSerializer(serializers.ModelSerializer):
    applicant = ApplicantSmallSerializer(many=False)
    experience = ExperienceSerializer(many=False)
    framework = FrameworkSerializer(many=False)
    project = ProjectSerializer(many=False)
    class Meta:
        model = ExperienceFrame
        fields = (
            'id',
            'experience',
            'applicant',
            'framework',
            'project'
        )