from rest_framework import serializers
from CV_ables_api.models import Education
from CV_ables_api.serializers import ApplicantSerializer
class EducationSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(many=False)
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