from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from CV_ables_api.models import Prospect
from CV_ables_api.serializers import ProspectSerializer
class ProspectView(ViewSet):
    def list(self, request):
        prospect = Prospect.objects.all()
        
        serializer = ProspectSerializer(
            prospect, many=True, context={'request': request}
        )
        return Response(serializer.data)