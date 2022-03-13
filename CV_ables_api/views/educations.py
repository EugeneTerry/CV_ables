from rest_framework.decorators import api_view
from rest_framework.response import Response
from CV_ables_api import serializers
from CV_ables_api.models import Education, education
from CV_ables_api.serializers import EducationSerializer

@api_view(['GET'])
def get_education_list(self):
    education = Education.objects.all()
    
    serializer = EducationSerializer(education, many=True)
    return Response(serializer.data)