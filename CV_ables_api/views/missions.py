from rest_framework.viewsets import ViewSet
from CV_ables_api.serializers import MissionSerializer
from rest_framework.response import Response
from CV_ables_api.models import Mission

class MissionView(ViewSet):
    def list(self, request):
        mission = Mission.objects.all()
        
        serializer = MissionSerializer(
            mission, many=True, context={'request': request}
            )
        return Response(serializer.data)