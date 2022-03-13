from rest_framework.decorators import api_view
from rest_framework.response import Response
from CV_ables_api.models import Description
from CV_ables_api.serializers import DescriptionSerializer

@api_view(['GET'])
def get_discription_list(self):
    description = Description.objects.all()
    
    serializer = DescriptionSerializer(description, many=True)
    return Response(serializer.data)