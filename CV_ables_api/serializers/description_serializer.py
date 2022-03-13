from rest_framework import serializers
from CV_ables_api.models import Description
from CV_ables_api.serializers.experience_serializer import ExperienceRawSerializer

class DescriptionSerializer(serializers.ModelSerializer):
    experience = ExperienceRawSerializer(many=False)
    class Meta:
        model = Description
        fields = (
            'id',
            'experience',
            'description_text'
        )