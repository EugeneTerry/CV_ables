from rest_framework import serializers
from CV_ables_api.models import Experience
from CV_ables_api.serializers.applicant_serializer import ApplicantSerializer


class ExperienceSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(many=False)
    class Meta:
        model = Experience
        fields = (
            'id',
            'applicant',
            'company'
        )
        
class ExperienceRawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            'id',
            'company'
        )