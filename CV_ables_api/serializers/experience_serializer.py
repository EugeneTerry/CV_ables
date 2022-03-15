from rest_framework import serializers
from CV_ables_api.models import Experience
from CV_ables_api.serializers import ApplicantSmallSerializer
from .jobtype_serializer import JobtypeSerializer
class ExperienceSerializer(serializers.ModelSerializer):
    applicant = ApplicantSmallSerializer(many=False)
    job_type = JobtypeSerializer(many=False)
    class Meta:
        model = Experience
        fields = (
            'id',
            'applicant',
            'job_type',
            'company',
            'job_title',
            'start_yr',
            'end_yr'
        )
class ExperienceRawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            'id',
            'job_type',
            'company',
            'job_title',
            'start_yr',
            'end_yr'
        )        
