from rest_framework.decorators import api_view
from rest_framework.response import Response
from CV_ables_api.models import Experience
from CV_ables_api.serializers import ExperienceSerializer

@api_view(['GET'])
def get_experience_list(self):
  experience = Experience.objects.all()
  
  serializer = ExperienceSerializer(experience, many=True)
  return Response(serializer.data)