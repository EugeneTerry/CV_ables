from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from CV_ables_api.models import Vita
from CV_ables_api.serializers import VitaSerializer
class VitaView(ViewSet):
    def list(self, request):
        vita = Vita.objects.all()
        
        serializer = VitaSerializer(
            vita, many=True, context={'request': request}
        )
        return Response(serializer.data)      