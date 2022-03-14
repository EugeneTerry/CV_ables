from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from CV_ables_api.models import Experience
from CV_ables_api.serializers import ExperienceSerializer
class ExerienceView(ViewSet):
  def list(self, request):
    experience = Experience.objects.all()
    
    serializer = ExperienceSerializer(
      experience, many=True, context={'request': request})
    return Response(serializer.data)