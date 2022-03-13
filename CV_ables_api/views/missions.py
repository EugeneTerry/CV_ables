from rest_framework.decorators import api_view
from CV_ables_api import serializers
from CV_ables_api.serializers import MissionSerializer
from rest_framework.response import Response
from CV_ables_api.models import Mission, mission

@api_view(['GET'])
def get_mission_list(self):
    mission = Mission.objects.all()
    
    serializer = MissionSerializer(mission, many=True)
    return Response(serializer.data)