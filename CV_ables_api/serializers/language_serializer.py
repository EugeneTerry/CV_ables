from rest_framework import serializers
from CV_ables_api.models import Language
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'id',
            'label'
        )