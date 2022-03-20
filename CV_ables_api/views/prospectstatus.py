from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from CV_ables_api.models import ProspectStatus, prospectstatus
from CV_ables_api.serializers import ProspectStatusSerializer
class ProspectStatusView(ViewSet):
    def list(self, request):
        prospectstatus = ProspectStatus.objects.all()
        
        serializer = ProspectStatusSerializer(
            prospectstatus, many=True, context={'request': request}
            )
        return Response(serializer.data)