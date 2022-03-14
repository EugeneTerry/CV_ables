from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from CV_ables_api import serializers
from CV_ables_api.models import Education, education
from CV_ables_api.serializers import EducationSerializer

class EducationView(ViewSet):
    def list(self, request):
        education = Education.objects.all()
        
        serializer = EducationSerializer(
            education, many=True, context={'request': request}
            )
        return Response(serializer.data)