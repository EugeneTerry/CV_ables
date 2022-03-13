from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from CV_ables_api.models import Framework
from CV_ables_api.serializers import FrameworkSerializer
class FrameworkView(ViewSet):
    def list(self, request):
        framework = Framework.objects.all()
        
        serializer = FrameworkSerializer(
            framework, many=True, context={'request': request}
            )
        return Response(serializer.data)