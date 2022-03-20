from rest_framework import serializers
from CV_ables_api.models import Prospect
from CV_ables_api.serializers import ApplicantSerializer
from CV_ables_api.serializers.prospectstatus_serializer import ProspectStatusSerializer

class ProspectSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(many=False)
    prospectstatus = ProspectStatusSerializer(many=False)
    class Meta:
        model = Prospect
        fields = (
            'id',
            'prospect_name',
            'listing_url',
            'markedvita',
            'notes',
            'prospectstatus',
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