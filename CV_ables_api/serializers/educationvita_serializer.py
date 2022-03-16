from rest_framework import serializers
from CV_ables_api.models import EducationVita
from .vita_serializer import VitaSerializer
from .education_serializer import EducationRawSerializer, EducationSerializer

class EducationVitaSerializer(serializers.ModelSerializer):
    vita = VitaSerializer(many=False)
    education = EducationRawSerializer(many=False)
    class Meta:
        model = EducationVita
        fields = (
            'id',
            'education',
            'vita'
        )