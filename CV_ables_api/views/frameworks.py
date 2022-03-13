from rest_framework.decorators import api_view
from rest_framework.response import Response
from CV_ables_api.models import Framework
from CV_ables_api.serializers import FrameworkSerializer

@api_view(['GET'])
def get_frameworks_list(self):
    framework = Framework.objects.all()
    
    serializer = FrameworkSerializer(framework, many=True)
    return Response(serializer.data)