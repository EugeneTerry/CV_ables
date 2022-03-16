from rest_framework import serializers
from CV_ables_api.models import Education
from CV_ables_api.serializers import ApplicantSmallSerializer
class EducationSerializer(serializers.ModelSerializer):
    applicant = ApplicantSmallSerializer(many=False)
    class Meta:
        model = Education
        fields = (
            'id',
            'applicant',
            'school_name',
            'city',
            'state',
            'diploma',
            'grad_year'
        )
        
class EducationRawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            'id',
            'school_name',
            'city',
            'state',
            'diploma',
            'grad_year'
        )