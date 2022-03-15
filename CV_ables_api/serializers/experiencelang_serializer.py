from rest_framework import serializers
from CV_ables_api.models import ExperienceLang
from CV_ables_api.serializers import ApplicantSmallSerializer, ExperienceSerializer, LanguageSerializer, ProjectSerializer

class ExperienceLangSerializer(serializers.ModelSerializer):
    applicant = ApplicantSmallSerializer(many=False)
    experience = ExperienceSerializer(many=False)
    language = LanguageSerializer(many=False)
    project = ProjectSerializer(many=False)
    class Meta:
        model = ExperienceLang
        fields = (
            'id',
            'experience',
            'applicant',
            'language',
            'project'
        )