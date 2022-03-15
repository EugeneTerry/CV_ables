from rest_framework import serializers
from CV_ables_api.models import ExperienceVita
from CV_ables_api.serializers import VitaSerializer, ExperienceSerializer


class ExperienceVitaSerializer(serializers.ModelSerializer):
    vita = VitaSerializer(many=False)
    experience = ExperienceSerializer(many=False)
    class Meta:
        model = ExperienceVita
        fields = (
            'id',
            'experience',
            'vita'
        )