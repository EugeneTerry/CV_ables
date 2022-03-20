from rest_framework import serializers
from CV_ables_api.models import ProspectStatus
class ProspectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProspectStatus
        fields = (
            'id',
            'label'
        )