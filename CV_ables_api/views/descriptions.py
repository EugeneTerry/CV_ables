from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from CV_ables_api.models import Description
from CV_ables_api.serializers import DescriptionSerializer

class DescriptionView(ViewSet):
    def list(self, request):
        description = Description.objects.all()
        
        serializer = DescriptionSerializer(
            description, many=True, context={'request': request}
            )
        return Response(serializer.data)