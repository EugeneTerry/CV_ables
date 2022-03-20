from rest_framework import serializers
from CV_ables_api.models import Prospect
from CV_ables_api.serializers import ApplicantSerializer

class ProspectSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(many=False)
    class Meta:
        model = Prospect
        fields = (
            'id',
            'prospect_name',
            'listing_url',
            'markedvita',
            'notes',
            'applicant'
        )
class ProspectSmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prospect
        fields = (
            'id',
            'prospect_name',
            'listing_url'
        )        