from rest_framework import serializers
from CV_ables_api.models import Framework
class FrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Framework
        fields = (
            'id',
            'label'
        )